# 导入matplotlib 和numpy模块
import numpy as np
from matplotlib import pyplot as plt

# 生成0-10之间 100个等差数
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
# 进行绘制正弦曲线
plt.plot(x, sin_y)

cos_y = np.cos(x)
plt.plot(x, cos_y)
# 保存成图片
plt.savefig('sin_cos.jpg')
plt.show()
