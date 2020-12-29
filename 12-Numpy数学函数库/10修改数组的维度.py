# 导入numpy模块
import numpy as np

# 通过reshape将一维数组修改为二、三维
# 创建一个一维数组
a = np.arange(1, 25)
print(a)
# 将一维修改为二维 (2,12) (4,6) (3,8)
# b=a.reshape(4,6)
b = a.reshape((3, 8))
print(b)

# 将一维修改为三维  (2,3,4)
c = a.reshape((2, 3, 4))
print(c)

# 通过np.reshape()进行修改
# bb=np.reshape(a,(3,8)) #将一维修改为二维
bb = np.reshape(a, (4, 3, 2))  # 将一维修改为三维
print(bb)

# 将多维数组修改为一维数组
# a=bb.reshape(24)
a = bb.reshape(-1)
print(a)
# 通过 ravel、flatten函数将多维数组转换为一维数组
# ravel
a = bb.ravel()
print(a)

# flatten
a = bb.flatten()
print(a)
