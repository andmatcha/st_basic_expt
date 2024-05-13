from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# データのパスを指定
data_path = Path(__file__).resolve().parent.joinpath("data/b.csv")
# CSVファイルの読み込み
df = pd.read_csv(data_path, header=0)

# グラフ用にデータを整理
x = np.array([0, 0.075, 0.15])
y1 = df[df["time"] == 0].drop(columns="time").to_numpy().flatten()
y2 = df[df["time"] == 20].drop(columns="time").to_numpy().flatten()
y3 = df[df["time"] == 40].drop(columns="time").to_numpy().flatten()
y4 = df[df["time"] == 600].drop(columns="time").to_numpy().flatten()

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.xlabel("測定位置 $\it{X}$ / m")
plt.ylabel("温度 $\it{T}$ / ℃")
plt.xticks(x)

# グラフを描画
plt.plot(x, y1, "ko-", markersize=3, lw=1, label="0s")
plt.plot(x, y2, "k^-", markersize=3, lw=1, label="20s")
plt.plot(x, y3, "kv-", markersize=3, lw=1, label="40s")
plt.plot(x, y4, "ks-", markersize=3, lw=1, label="600s")
plt.legend()

plt.show()
