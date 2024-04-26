# 入力 矩形波 1.0V 500Hz 入力波を描画

import matplotlib.pyplot as plt
import numpy as np

# グラフの設定

# 日本語が文字化けしないようにフォントを設定
plt.rcParams["font.family"] = "Hiragino Sans"
# x軸のラベル, $\it{}$ とすると{}内の文字が斜体になる
plt.xlabel("時間 $\it{t}$ / s")
# y軸のラベル
plt.ylabel("入力電圧 $\it{u}$ / V")
# 内向き目盛り
plt.tick_params(direction="in")

# データ
x = np.array([0, 1, 1, 2, 2, 3, 3, 4])
y = np.array([1, 1, -1, -1, 1, 1, -1, -1])

# 描画
plt.plot(x, y, "k-")  # k:黒色 o:丸印 -:実線
plt.show()
