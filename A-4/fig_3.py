# ReとStの関係

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# データ
data_path = Path(__file__).resolve().parent.joinpath("data/3.csv")
# CSVファイルの読み込み
df = pd.read_csv(data_path, header=0)

# グラフ用にデータを整理
x = df["Re"]  # レイノルズ数
y = df["St"]  # ストロハル数

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.xlabel("レイノルズ数 $\it{Re}$")
plt.ylabel("ストロハル数 $\it{St}$")

plt.xticks(x)
plt.grid(True, axis="x", which="both", ls="--")
plt.ylim(0, 1)

# グラフを描画
plt.plot(x, y, "ko-", lw=1)
plt.show()
