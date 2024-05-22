import matplotlib.pyplot as plt
import numpy as np

# データ
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([1.5, 2.5, 3.5, 4.5])
y1 = np.array([7.35, 7.05, 6.90, 7.00, 7.45])
y2 = np.array([12.74 - 10.05, 13.57 - 10.00, 16.18 - 9.99, 13.30 - 9.98])

# グラフの設定
# 日本語が文字化けしないようにフォントを設定
plt.rcParams["font.family"] = "Hiragino Sans"

fig, ax1 = plt.subplots()
plt.grid(True, axis="x", which="both", ls="--")
plt.tick_params(direction="in")
ax1.set_xlabel("標点番号", fontsize=10)
ax1.set_ylabel("試験後の直径(mm)", fontsize=10)
ax1.plot(x1, y1, "ko-", markersize=6, lw=1, label="直径")

ax2 = ax1.twinx()
plt.tick_params(direction="in")
ax2.set_ylabel("標点間の伸び量(mm)", fontsize=10)
ax2.plot(x2, y2, "k^-", markersize=6, lw=1, label="伸び量")

plt.xticks([1, 2, 3, 4, 5])

# 凡例
handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
ax1.legend(handler1 + handler2, label1 + label2)

plt.show()
