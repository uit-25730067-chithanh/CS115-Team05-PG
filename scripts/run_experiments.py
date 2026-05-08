import argparse
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "sources"
SOURCE_DIR_STRING = str(SOURCE_DIR)
sys.path = [path for path in sys.path if path != SOURCE_DIR_STRING]
sys.path.insert(0, SOURCE_DIR_STRING)

from train import (
    DEFAULT_ENV,
    plot_learning_curve,
    train_reinforce,
)


DEFAULT_EPISODES = 500
DEFAULT_LRS = [1e-2, 1e-3]
DEFAULT_GAMMAS = [0.95, 0.99]
DEFAULT_HIDDEN_DIMS = [64, 128]
DEFAULT_SEEDS = [42]
MAX_RUNS_WITHOUT_EXTRA_APPROVAL = 16
LAST_REWARD_WINDOW = 50


def positive_int(value):
    parsed_value = int(value)
    if parsed_value < 1:
        raise argparse.ArgumentTypeError("value must be at least 1")
    return parsed_value


def parse_args():
    parser = argparse.ArgumentParser(description="Run compact REINFORCE hyperparameter experiments.")
    parser.add_argument("--env", default=DEFAULT_ENV)
    parser.add_argument("--episodes", type=positive_int, default=DEFAULT_EPISODES)
    parser.add_argument("--lrs", type=float, nargs="+", default=DEFAULT_LRS)
    parser.add_argument("--gammas", type=float, nargs="+", default=DEFAULT_GAMMAS)
    parser.add_argument("--hidden-dims", type=positive_int, nargs="+", default=DEFAULT_HIDDEN_DIMS)
    parser.add_argument("--seeds", type=int, nargs="+", default=DEFAULT_SEEDS)
    parser.add_argument("--save-root", default=None)
    return parser.parse_args()


def select_device_name():
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def build_grid(args):
    configs = []
    for lr in args.lrs:
        for gamma in args.gammas:
            for hidden_dim in args.hidden_dims:
                for seed in args.seeds:
                    configs.append({
                        "env": args.env,
                        "episodes": args.episodes,
                        "lr": lr,
                        "gamma": gamma,
                        "hidden_dim": hidden_dim,
                        "seed": seed,
                    })
    if len(configs) > MAX_RUNS_WITHOUT_EXTRA_APPROVAL:
        raise ValueError(
            f"Refusing to run {len(configs)} configs; keep the grid at "
            f"{MAX_RUNS_WITHOUT_EXTRA_APPROVAL} runs or fewer without extra approval."
        )
    return configs


def summarize_rewards(rewards):
    # Use the final 50 episodes as the convergence window, matching the training log cadence.
    last_rewards = rewards[-LAST_REWARD_WINDOW:]
    return {
        "mean_last_50": float(np.mean(last_rewards)) if last_rewards else 0.0,
        "std_last_50": float(np.std(last_rewards)) if last_rewards else 0.0,
        "best_reward": float(np.max(rewards)) if rewards else 0.0,
        "final_reward": float(rewards[-1]) if rewards else 0.0,
    }


def format_config(config):
    return f"lr={config['lr']}, gamma={config['gamma']}, hidden_dim={config['hidden_dim']}"


def write_summary(summary_path, experiment_root, configs, results, device_name):
    # Rank by stable recent performance first, variance second, and peak reward only as a tie-breaker.
    ranked_results = sorted(
        results,
        key=lambda result: (
            -result["mean_last_50"],
            result["std_last_50"],
            -result["best_reward"],
        ),
    )
    best = ranked_results[0] if ranked_results else None

    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# REINFORCE Hyperparameter Experiment Summary\n\n")
        f.write(f"- Experiment timestamp: `{experiment_root.name}`\n")
        f.write(f"- Device: `{device_name}`\n")
        f.write(f"- Total runs: `{len(results)}`\n\n")

        f.write("## Exact Grid\n\n")
        f.write(f"- Environment: `{configs[0]['env'] if configs else DEFAULT_ENV}`\n")
        f.write(f"- Episodes: `{configs[0]['episodes'] if configs else DEFAULT_EPISODES}`\n")
        f.write(f"- Learning rates: `{sorted({config['lr'] for config in configs})}`\n")
        f.write(f"- Gammas: `{sorted({config['gamma'] for config in configs})}`\n")
        f.write(f"- Hidden dimensions: `{sorted({config['hidden_dim'] for config in configs})}`\n")
        f.write(f"- Seeds: `{sorted({config['seed'] for config in configs})}`\n\n")

        f.write("## Ranked Results\n\n")
        f.write("| Rank | Config | Seed | Mean Last-50 | Std Last-50 | Best Reward | Run Dir |\n")
        f.write("| ---: | ------ | ---: | -----------: | ----------: | ----------: | ------- |\n")
        for rank, result in enumerate(ranked_results, start=1):
            run_dir = Path(result["run_dir"]).relative_to(experiment_root)
            f.write(
                f"| {rank} | `{format_config(result['config'])}` | {result['config']['seed']} | "
                f"{result['mean_last_50']:.4f} | {result['std_last_50']:.4f} | "
                f"{result['best_reward']:.4f} | `{run_dir}` |\n"
            )

        f.write("\n## Selected Best Config\n\n")
        if best is None:
            f.write("No completed runs.\n")
        else:
            f.write(f"- Config: `{format_config(best['config'])}`\n")
            f.write(f"- Seed: `{best['config']['seed']}`\n")
            f.write(f"- Run dir: `{Path(best['run_dir']).relative_to(experiment_root)}`\n\n")
            f.write("## Rationale\n\n")
            f.write(
                "Selected by highest mean reward over the last 50 episodes, "
                "then lower last-50 standard deviation, then best reward as tie-breaker.\n\n"
            )

        f.write("## Limitations\n\n")
        f.write("- The default experiment uses one seed, so RL variance can still affect ranking.\n")
        f.write("- The grid is intentionally compact for academic review and local runtime.\n")

    return ranked_results


def main():
    args = parse_args()
    configs = build_grid(args)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    experiment_root = Path(args.save_root) if args.save_root else PROJECT_ROOT / "outputs" / "experiments" / timestamp
    if experiment_root.exists() and any(experiment_root.iterdir()):
        raise ValueError(f"Refusing to write into non-empty experiment root: {experiment_root}")
    experiment_root.mkdir(parents=True, exist_ok=True)

    results = []
    for index, config in enumerate(configs, start=1):
        run_dir = experiment_root / f"config-{index:03d}-seed-{config['seed']}"
        if run_dir.exists():
            raise ValueError(f"Refusing to overwrite existing run directory: {run_dir}")
        print(f"Running config {index}/{len(configs)}: {format_config(config)}, seed={config['seed']}")
        rewards = train_reinforce(
            env_name=config["env"],
            max_episodes=config["episodes"],
            lr=config["lr"],
            gamma=config["gamma"],
            hidden_dim=config["hidden_dim"],
            seed=config["seed"],
            save_dir=str(run_dir),
        )
        plot_learning_curve(rewards, save_path=run_dir / "training_curve.png", seed=config["seed"])
        metrics = summarize_rewards(rewards)
        results.append({
            "config": config,
            "run_dir": str(run_dir),
            **metrics,
        })

    summary_path = experiment_root / "summary.md"
    ranked_results = write_summary(summary_path, experiment_root, configs, results, select_device_name())
    print(f"Experiment summary saved to: {summary_path}")
    if ranked_results:
        best = ranked_results[0]
        print(
            "Best config: "
            f"{format_config(best['config'])}, seed={best['config']['seed']}, "
            f"mean_last_50={best['mean_last_50']:.2f}"
        )


if __name__ == "__main__":
    main()
