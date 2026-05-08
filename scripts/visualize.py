import argparse
from datetime import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WINDOW = 50
DPI = 300
GRID_ALPHA = 0.35
COLORS = {
    "raw": "#6B7280",
    "best": "#2563EB",
    "baseline": "#B45309",
    "bar": "#4B5563",
    "accent": "#047857",
}


def positive_int(value):
    parsed_value = int(value)
    if parsed_value < 1:
        raise argparse.ArgumentTypeError("value must be at least 1")
    return parsed_value


def parse_args():
    parser = argparse.ArgumentParser(description="Generate report-ready figures from REINFORCE output logs.")
    parser.add_argument("--experiment", required=True, help="Path to an outputs/experiments/... directory.")
    parser.add_argument("--baseline", default=None, help="Optional path to a baseline_log.txt file.")
    parser.add_argument("--output-dir", default=None, help="Optional output directory for generated figures.")
    parser.add_argument("--window", type=positive_int, default=DEFAULT_WINDOW, help="Moving-average window size.")
    parser.add_argument("--force", action="store_true", help="Allow overwriting known figure files in a non-empty output directory.")
    return parser.parse_args()


def read_reward_log(path):
    rewards = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.replace(",", "\t").split()
            if len(parts) < 2:
                raise ValueError(f"Invalid reward row in {path} at line {line_number}: {stripped}")
            rewards.append(float(parts[1]))
    if not rewards:
        raise ValueError(f"No rewards found in {path}")
    return rewards


def read_config(path):
    config = {}
    if not path.exists():
        return config
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if ":" not in line:
                continue
            key, value = line.strip().split(":", 1)
            config[key.strip()] = value.strip()
    return config


def moving_average(values, window):
    if not values:
        return np.array([]), np.array([])
    effective_window = min(window, len(values))
    rewards = np.asarray(values, dtype=float)
    kernel = np.ones(effective_window) / effective_window
    smoothed = np.convolve(rewards, kernel, mode="valid")
    episodes = np.arange(effective_window, len(values) + 1)
    return episodes, smoothed


def summarize(values, window):
    last_values = values[-window:]
    return {
        "mean_last_window": float(np.mean(last_values)),
        "std_last_window": float(np.std(last_values)),
        "best_reward": float(np.max(values)),
        "final_reward": float(values[-1]),
        "episodes": len(values),
    }


def format_config(config, fallback):
    if not config:
        return fallback
    parts = []
    for key in ("lr", "gamma", "hidden_dim", "seed"):
        if key in config:
            parts.append(f"{key}={config[key]}")
    return ", ".join(parts) if parts else fallback


def find_runs(experiment_dir, window):
    reward_paths = sorted(experiment_dir.glob("**/rewards.txt"))
    runs = []
    for reward_path in reward_paths:
        rewards = read_reward_log(reward_path)
        run_dir = reward_path.parent
        config = read_config(run_dir / "run_config.txt")
        relative_name = str(run_dir.relative_to(experiment_dir))
        runs.append({
            "run_dir": run_dir,
            "name": relative_name,
            "label": format_config(config, relative_name),
            "rewards": rewards,
            "config": config,
            **summarize(rewards, window),
        })
    if not runs:
        raise ValueError(f"No rewards.txt files found under experiment directory: {experiment_dir}")
    return sorted(
        runs,
        key=lambda run: (-run["mean_last_window"], run["std_last_window"], -run["best_reward"]),
    )


def save_figure(path):
    plt.tight_layout()
    plt.savefig(path, dpi=DPI)
    plt.close()
    print(f"Saved figure: {path}")


def plot_learning_curve_best(best_run, output_path, window):
    rewards = best_run["rewards"]
    episodes = np.arange(1, len(rewards) + 1)
    ma_episodes, smoothed = moving_average(rewards, window)
    plt.figure(figsize=(10, 5.5))
    plt.plot(episodes, rewards, color=COLORS["raw"], alpha=0.35, linewidth=1.0, label="Raw reward")
    plt.plot(ma_episodes, smoothed, color=COLORS["best"], linewidth=2.2, label=f"Moving average ({min(window, len(rewards))})")
    plt.title(f"Best REINFORCE Learning Curve\n{best_run['label']}")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.legend()
    plt.grid(True, alpha=GRID_ALPHA)
    save_figure(output_path)


def plot_baseline_vs_trained(baseline_rewards, best_run, output_path, window):
    baseline_episodes, baseline_ma = moving_average(baseline_rewards, window)
    trained_episodes, trained_ma = moving_average(best_run["rewards"], window)
    plt.figure(figsize=(10, 5.5))
    plt.plot(baseline_episodes, baseline_ma, color=COLORS["baseline"], linewidth=2.0, label=f"Random baseline MA ({min(window, len(baseline_rewards))})")
    plt.plot(trained_episodes, trained_ma, color=COLORS["best"], linewidth=2.0, label=f"Best trained MA ({min(window, len(best_run['rewards']))})")
    plt.axhline(float(np.mean(baseline_rewards)), color=COLORS["baseline"], linestyle="--", alpha=0.65, label="Baseline mean")
    plt.title("Random Baseline vs Best Trained Policy")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.legend()
    plt.grid(True, alpha=GRID_ALPHA)
    save_figure(output_path)


def plot_hp_comparison(runs, output_path, window):
    labels = [run["label"] for run in runs]
    means = [run["mean_last_window"] for run in runs]
    errors = [run["std_last_window"] for run in runs]
    x = np.arange(len(runs))
    width = max(9, min(16, len(runs) * 1.35))
    plt.figure(figsize=(width, 5.8))
    plt.bar(x, means, yerr=errors, color=COLORS["bar"], alpha=0.85, capsize=4, label=f"Mean ± std, last {window}")
    plt.xticks(x, labels, rotation=35, ha="right")
    plt.title("Hyperparameter Comparison by Recent Reward")
    plt.xlabel("Run Configuration")
    plt.ylabel("Total Reward")
    plt.legend()
    plt.grid(axis="y", alpha=GRID_ALPHA)
    save_figure(output_path)


def plot_summary_grid(runs, output_path, window):
    rows = [[
        str(index),
        run["label"],
        f"{run['mean_last_window']:.2f}",
        f"{run['std_last_window']:.2f}",
        f"{run['best_reward']:.2f}",
        str(run["episodes"]),
    ] for index, run in enumerate(runs, start=1)]
    headers = ["Rank", "Config", f"Mean Last-{window}", f"Std Last-{window}", "Best", "Episodes"]
    height = max(3.2, 1.0 + len(rows) * 0.48)
    plt.figure(figsize=(12, height))
    plt.axis("off")
    table = plt.table(cellText=rows, colLabels=headers, loc="center", cellLoc="left")
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1, 1.35)
    plt.title("REINFORCE Experiment Ranking Summary", pad=18)
    save_figure(output_path)


def write_summary(output_dir, experiment_dir, baseline_path, runs, generated_files, window):
    summary_path = output_dir / "figure_summary.txt"
    best_run = runs[0]
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("REINFORCE Figure Generation Summary\n")
        f.write("====================================\n\n")
        f.write(f"Experiment: {experiment_dir}\n")
        f.write(f"Baseline: {baseline_path if baseline_path else 'not provided'}\n")
        f.write(f"Window: {window}\n")
        f.write(f"Best run: {best_run['name']}\n")
        f.write(f"Best config: {best_run['label']}\n")
        f.write(f"Mean last window: {best_run['mean_last_window']:.4f}\n")
        f.write(f"Std last window: {best_run['std_last_window']:.4f}\n")
        f.write(f"Best reward: {best_run['best_reward']:.4f}\n\n")
        f.write("Generated files:\n")
        for file_path in generated_files:
            f.write(f"- {file_path.name}\n")
    print(f"Saved summary: {summary_path}")


def main():
    args = parse_args()
    experiment_dir = Path(args.experiment).expanduser().resolve()
    if not experiment_dir.exists() or not experiment_dir.is_dir():
        raise FileNotFoundError(f"Experiment directory does not exist: {experiment_dir}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else PROJECT_ROOT / "outputs" / "figures" / timestamp
    if args.output_dir and output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        raise ValueError(f"Refusing to write into non-empty output directory without --force: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    runs = find_runs(experiment_dir, args.window)
    best_run = runs[0]
    generated_files = []

    learning_curve_path = output_dir / "learning_curve_best.png"
    plot_learning_curve_best(best_run, learning_curve_path, args.window)
    generated_files.append(learning_curve_path)

    baseline_path = None
    if args.baseline:
        baseline_path = Path(args.baseline).expanduser().resolve()
        if baseline_path.exists() and baseline_path.is_file():
            baseline_rewards = read_reward_log(baseline_path)
            baseline_figure_path = output_dir / "baseline_vs_trained.png"
            plot_baseline_vs_trained(baseline_rewards, best_run, baseline_figure_path, args.window)
            generated_files.append(baseline_figure_path)
        else:
            print(f"Warning: baseline log not found; skipping baseline_vs_trained.png: {baseline_path}")
    else:
        print("Warning: --baseline was not provided; skipping baseline_vs_trained.png")

    hp_comparison_path = output_dir / "hp_comparison.png"
    plot_hp_comparison(runs, hp_comparison_path, args.window)
    generated_files.append(hp_comparison_path)

    summary_grid_path = output_dir / "summary_grid.png"
    plot_summary_grid(runs, summary_grid_path, args.window)
    generated_files.append(summary_grid_path)

    write_summary(output_dir, experiment_dir, baseline_path, runs, generated_files, args.window)
    print(f"Figures saved to: {output_dir}")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError) as error:
        raise SystemExit(f"Error: {error}")
