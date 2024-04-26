# 入力 矩形波 5.0V 500Hz 出力波(台形波)を描画

import matplotlib.pyplot as plt
import numpy as np

# グラフの設定

# 日本語が文字化けしないようにフォントを設定
plt.rcParams["font.family"] = "Hiragino Sans"
# x軸のラベル, $\it{}$ とすると{}内の文字が斜体になる
plt.xlabel("時間 $\it{t}$ / s")
# y軸のラベル
plt.ylabel("出力電圧 $\it{y}$ / V")
# 内向き目盛り
plt.tick_params(direction="in")

# データ
x = np.array([0, 0.2, 0.5, 0.8, 1.2, 1.5, 1.8, 2.2, 2.5, 2.8, 3.2, 3.5, 3.8, 4])
y = np.array([14, 14, 0, -14, -14, 0, 14, 14, 0, -14, -14, 0, 14, 14 ])

# 描画
plt.plot(x, y, "k-")  # k:黒色 o:丸印 -:実線
plt.show()
