from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# データ
data_path_1 = Path(__file__).resolve().parent.joinpath("data/4.csv")
# CSVファイルの読み込み
df_1 = pd.read_csv(data_path_1, header=0)

# グラフ用にデータを整理

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.xlabel("周波数 $\it{f} [kHz] $")
plt.ylabel("消費電力 $\it{P} [W] $")

# グラフを描画
plt.plot(df_1["f"], df_1["P"], "k.-", lw=0.5, markersize=4, label="測定1")
plt.show()
