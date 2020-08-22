# 导入numpy
import numpy as np

# range的使用range(start,end,step) [start,end)
a = list(range(1, 10))  # 步长是1
print(a)
b = list(range(10))  # 默认的是从0开始 ，步长是1
print(b)
c = list(range(1, 10, 3))
print(c)

# arange创建数组
# 使用arange创建1,10的数组
a = np.arange(1, 11)
print(a)

# 设置step
b = np.arange(1, 11, 2)
print(b)

# 设置dtype
c = np.arange(10, 20, 2, dtype=float)
print(c)
