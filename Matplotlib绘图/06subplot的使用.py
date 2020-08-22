# 导入模块
import numpy as np
from matplotlib import pyplot as plt

# 创建0-10中100个等差数
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
# 绘制正弦曲线
# 对画布进行分区 将画布分为2行2列  画到区1
plt.subplot(2, 2, 1)
# 修改x、y轴的坐标
plt.xlim(-5, 20)
plt.ylim(-2, 2)
plt.plot(x, sin_y)

plt.subplot(2, 2, 4)
plt.plot(x, np.cos(x))
plt.show()
