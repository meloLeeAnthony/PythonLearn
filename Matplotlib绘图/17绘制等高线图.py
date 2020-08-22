# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 创建x y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
# 计算x y相交的点 X Y
X, Y = np.meshgrid(x, y)
# 计算Z
Z = np.sqrt(X ** 2 + Y ** 2)
# 绘制等高线图
# plt.contour(X,Y,Z)
plt.contourf(X, Y, Z)
plt.show()
