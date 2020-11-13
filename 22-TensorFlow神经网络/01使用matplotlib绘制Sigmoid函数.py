import matplotlib.pyplot as plt
import numpy as np


# 定义sigmoid函数
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


x = np.arange(-10, 10)
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(x, sigmoid(x), 'r')
plt.show()
