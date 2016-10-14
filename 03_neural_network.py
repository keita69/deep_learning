import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
plt.ylim(-0.1, 1.1) # y 軸の範囲を指定
y1 = step_function(x)
y2 = sigmoid(x)

# グラフの描画
plt.plot(x, y1, label="ステップ関数")
plt.plot(x, y2, linestyle = "--", label="シグモイド関数") # 破線で描画
plt.xlabel("x") # x 軸のラベル
plt.ylabel("y") # y 軸のラベル
plt.title('ステップ関数とシグモイド関数') # タイトル
plt.legend()
plt.show()