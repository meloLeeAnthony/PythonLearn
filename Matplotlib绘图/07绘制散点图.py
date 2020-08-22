# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 生成0-10之间100个等差数
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
# 绘制正弦的曲线
plt.plot(x, sin_y, 'o')
# 绘制散点图
# plt.scatter(x, sin_y)
plt.show()
'''
从上面的示例可以看到，使用plot绘制和使用scatter绘制出来的图形是没有区别的，
但是使用plot绘制图形的速度优于scatter，所以如果画一堆点，而且点的形式没有差别，那么我们
使用plot，如果点的形式有差别(指点的大小和颜色不同)则必须使用scatter
'''
