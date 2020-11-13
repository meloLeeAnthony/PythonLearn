# 导入模块
import matplotlib.pyplot as plt
# 导入3d包
from mpl_toolkits.mplot3d import Axes3D

# 创建X  Y  Z
X = [1, 1, 2, 2]
Y = [3, 4, 4, 3]
Z = [1, 100, 1, 1]
figure = plt.figure()
# 创建Axes3D对象
ax = Axes3D(figure)
ax.plot_trisurf(X, Y, Z)
plt.show()
