from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# データ
data_path = Path(__file__).resolve().parent.joinpath("data/3.csv")
# CSVファイルの読み込み
df = pd.read_csv(data_path, header=0)

# グラフ用にデータを整理
x = df[df["n"] % 1 == 0]
y = x["A"]
y_ideal = 1 / x["n"]

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.xlabel("次数 $\it{n}$")
plt.ylabel("$\it{A_n / A_1}$")
plt.xlim(1, 60)

# グラフを描画
plt.plot(x["n"], y, "ko-", lw=1, label="実験値")
plt.plot(x["n"], y_ideal, "k^--", lw=1, label="理論値")
plt.legend()
plt.show()


