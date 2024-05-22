from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# データのパスを指定
data_path = Path(__file__).resolve().parent.joinpath("data/1.csv")
# CSVファイルの読み込み
df = pd.read_csv(data_path, header=0)

# グラフ用にデータを整理
x = df["epsilon"] # ひずみ [m/m]
y = df["sigma"] # 応力 [MPa]

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.xlabel("ひずみ $\it{\epsilon}$")
plt.ylabel("応力 $\it{\sigma}$ [MPa]")

# グラフを描画
plt.plot(x, y, "k-", lw=1)

plt.show()
