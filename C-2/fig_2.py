import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import numpy as np

# データ
data_path = Path(__file__).resolve().parent.joinpath("data/2.csv")
# CSVファイルの読み込み
df = pd.read_csv(data_path, header=0)

# グラフ用にデータを整理
x = df["x"]  # 沸点
y = df["y"]  # 保持時間の対数

# 近似直線
coefficient = np.polyfit(x, y, 1)  # 係数
linear_regression = np.poly1d(coefficient)(x)  # 近似直線

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.xlabel("沸点")
plt.ylabel("保持時間の対数")

plt.xticks(x)
plt.grid(True, axis="x", which="both", ls="--")

# グラフを描画
plt.plot(x, y, "ko")
plt.plot(x, linear_regression, "k-", lw=1)
plt.show()
