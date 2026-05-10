# Teams Message to Quỳnh

Hi Quỳnh,

Anh vừa review nhanh bản PDF report mới nhất. Khung báo cáo hiện ổn rồi, đặc biệt phần Introduction và phần đầu Mathematical Foundation. Phần team mình có thể hỗ trợ Quỳnh nhiều nhất là Chapter III Methods và Chapter IV Experiments & Results vì các phần này cần bám sát code/output thật.

Một vài điểm Quỳnh check giúp anh trước:

- Check lại List of Figures/Tables để đảm bảo không còn mục template/stale và mọi figure đều thuộc CartPole/REINFORCE.
- Abstract còn các placeholder như `To be updated` hoặc `[Link]` thì thay bằng nội dung final/link repo final.
- Contribution percentage table hiện cần điền phần trăm đóng góp.
- Chapter III và IV hiện nên bổ sung nội dung từ implementation thật: REINFORCE, PolicyNetwork, CartPole-v1, training pipeline, baseline, learning curve.
- Tránh dùng wording `critic` hoặc `actor-critic` vì code hiện tại dùng normalized returns để giảm variance, không có critic network.
- Kết quả mới nhất có thể đưa vào report: random baseline mean reward `23.28`; trained REINFORCE đạt `mean_last_100 = 476.00`, vượt threshold CartPole-v1 `475`; best/final reward đều `500`.

Anh đã chuẩn bị sẵn một bản nội dung tiếng Anh paste-ready cho Chapter III/IV + bảng số liệu + caption figure. Quỳnh có thể copy vào Word rồi chỉnh lại văn phong cho đồng nhất với report.

Figure nên chèn:

- `outputs/baseline_20260510_011932/baseline_curve.png`
- `outputs/run_20260510_011946/training_curve.png`

Nếu Quỳnh muốn, anh sẽ review lại bản Word sau khi Quỳnh paste nội dung và export PDF lần tiếp theo.
