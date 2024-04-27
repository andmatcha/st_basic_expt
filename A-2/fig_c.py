from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# データのパスを指定
data_path = Path(__file__).resolve().parent.joinpath("data/c.csv")
# CSVファイルの読み込み
df = pd.read_csv(data_path, header=0)

# グラフ用にデータを整理
x = df["time"]
y1 = df["T1"]
y2 = df["T2"]
y3 = df["T3"]

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.xlabel("経過時間 / s")
plt.ylabel("温度 $\it{T}$ / ℃")

# グラフを描画
plt.plot(x, y1, "ko-", markersize=3, lw=1, label="$T_{1}$")
plt.plot(x, y2, "k^-", markersize=3, lw=1, label="$T_{2}$")
plt.plot(x, y3, "ks-", markersize=3, lw=1, label="$T_{3}$")
plt.legend()

plt.show()
