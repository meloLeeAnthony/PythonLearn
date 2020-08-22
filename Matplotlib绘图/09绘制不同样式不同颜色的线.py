# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 创建x
x = np.linspace(0, 10, 100)
plt.plot(x, x + 0, '--g')
plt.plot(x, x + 1, '-.r')
plt.plot(x, x + 2, ':b')
plt.plot(x, x + 3, '.k')
plt.plot(x, x + 4, ',c')
plt.plot(x, x + 5, '*y')
plt.show()
