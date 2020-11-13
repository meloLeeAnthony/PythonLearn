# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 生成x y
np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5, 5, 5)
# 添加颜色
v_bar = plt.bar(x, y, color='blue')

# 对y值大于0设置为蓝色  小于0的柱设置为绿色
for bar, height in zip(v_bar, y):
    if height < 0:
        bar.set(color='green')

# 在0位置水平方向添加red的线条
plt.axhline(0, color='red', linewidth=2)
plt.show()
