from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# データ
data_path_long = Path(__file__).resolve().parent.joinpath("data/2.csv")
data_path_short = Path(__file__).resolve().parent.joinpath("data/4.csv")
data_path_pulse = Path(__file__).resolve().parent.joinpath("data/5.csv")
# CSVファイルの読み込み
df_long = pd.read_csv(data_path_long, header=0)
df_short = pd.read_csv(data_path_short, header=0)
df_pulse = pd.read_csv(data_path_pulse, header=0)

# グラフ用にデータを整理
filtered_long = df_long[df_long["n"] % 2 == 1]
filtered_short = df_short[df_short["n"] % 2 ==1]
filtered_pulse = df_pulse[df_pulse["n"] % 2 ==1]

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.xlabel("次数 $\it{n}$")
plt.ylabel("$\it{A_n / A_1}$")
plt.xlim(1, 60)

# グラフを描画
plt.plot(filtered_long["n"], filtered_long["A"], "k^-", lw=0.8, label="幅の広い三角波")
plt.plot(filtered_short["n"], filtered_short["A"], "kv-", lw=0.8, label="幅の狭い三角波")
plt.plot(filtered_pulse["n"], filtered_pulse["A"], "ko-", lw=0.8, label="パルス波")
plt.legend()
plt.show()
