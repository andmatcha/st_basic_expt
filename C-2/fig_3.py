import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import numpy as np

# データ
data_path = Path(__file__).resolve().parent.joinpath("data/3.csv")
# CSVファイルの読み込み
df = pd.read_csv(data_path, header=0)

# グラフ用にデータを整理
ethanol = df[df["alcohol"] == "エタノール"]
propanol = df[df["alcohol"] == "1-プロパノール"]
butanol = df[df["alcohol"] == "1-ブタノール"]
pentanol = df[df["alcohol"] == "1-ペンタノール"]

# 近似直線
coefficient_ethanol = np.polyfit(ethanol["mol"], ethanol["peak"], 1)
coefficient_propanol = np.polyfit(propanol["mol"], propanol["peak"], 1)
coefficient_butanol = np.polyfit(butanol["mol"], butanol["peak"], 1)
coefficient_pentanol = np.polyfit(pentanol["mol"], pentanol["peak"], 1)

print([coefficient_ethanol, coefficient_propanol, coefficient_butanol, coefficient_pentanol])

linear_regression_ethanol = np.poly1d(coefficient_ethanol)(ethanol["mol"])
linear_regression_propanol = np.poly1d(coefficient_propanol)(propanol["mol"])
linear_regression_butanol = np.poly1d(coefficient_butanol)(butanol["mol"])
linear_regression_pentanol = np.poly1d(coefficient_pentanol)(pentanol["mol"])

# グラフ設定
plt.rcParams["font.family"] = "Hiragino Mincho ProN"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.xlabel("物質量 [$×10^{-6}$ mol]")
plt.ylabel("ピーク面積 [$×10^5$ μV sec]")

# グラフを描画
plt.plot(ethanol["mol"], ethanol["peak"], "ko")
plt.plot(ethanol["mol"], linear_regression_ethanol, "k-", lw=1)
plt.plot(propanol["mol"], propanol["peak"], "k^")
plt.plot(propanol["mol"], linear_regression_propanol, "k-", lw=1)
plt.plot(butanol["mol"], butanol["peak"], "ks")
plt.plot(butanol["mol"], linear_regression_butanol, "k-", lw=1)
plt.plot(pentanol["mol"], pentanol["peak"], "kv")
plt.plot(pentanol["mol"], linear_regression_pentanol, "k-", lw=1)
plt.show()
