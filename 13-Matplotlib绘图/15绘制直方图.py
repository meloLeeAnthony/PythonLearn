# 也直方图关注的是分布，并不关心具体的某个值，而柱状图关心的是具体的某个值
# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 生成1000个标志的正太分布随机数
x = np.random.randn(1000)
# plt.hist(x)
# 修改柱的宽度  使用bins
plt.hist(x, bins=100)  # 10个柱装在一起
plt.show()
