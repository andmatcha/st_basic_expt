from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# データ
data_path_1 = Path(__file__).resolve().parent.joinpath("data/1-1.csv")
data_path_2 = Path(__file__).resolve().parent.joinpath("data/1-2.csv")
data_path_3 = Path(__file__).resolve().parent.joinpath("data/1-3.csv")
# CSVファイルの読み込み
df_1 = pd.read_csv(data_path_1, header=0)
df_2 = pd.read_csv(data_path_2, header=0)
df_3 = pd.read_csv(data_path_3, header=0)

# グラフ用にデータを整理

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.xlabel("周波数 $\it{f} [kHz]$")
plt.ylabel("電流 $\it{I} [mA]$")

# グラフを描画
plt.plot(df_1["f"], df_1["I"], "k.-", lw=0.5, markersize=4, label="測定1")
plt.plot(df_2["f"], df_2["I"], "kx-", lw=0.5, markersize=4, label="測定2")
plt.plot(df_3["f"], df_3["I"], "k+-", lw=0.5, markersize=4, label="測定3")
plt.legend()
plt.show()
