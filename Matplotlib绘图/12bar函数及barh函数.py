# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 生成x y
np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5, 5, 5)
# 将画布分为1行2列  在第一个区域画bar
plt.subplot(1, 2, 1)
# 添加颜色
plt.bar(x, y, color='blue')
# 在0位置水平方向添加蓝色的线条
plt.axhline(0, color='blue', linewidth=2)

# 在第二个区域画barh
# barh  将y和x进行对换，竖着方向为x轴
plt.subplot(1, 2, 2)
plt.barh(x, y, color='red')
# 在0位置垂直方向添加红色线条
plt.axvline(0, color='red', linewidth=2)

plt.show()
