# 导入numpy模块
import numpy as np

# 创建二维数组
a = np.arange(1, 25).reshape(8, 3)
print(a)
print('transpose函数进行数组转置 a[i][j]---a[j][i]')
b = a.transpose()
print(b, b.shape)

# 可以使用 .T
print(a.T)

# numpy中transpose()
c = np.transpose(a)
print(c, c.shape)

# 多维数组进行转置
a = a.reshape(2, 3, 4)
print(a, a.shape)
print('对于三维a[i][j][k] 进行转置 默认的将i和k交换')
b = np.transpose(a)
print(b, b.shape)
# (2,3,4)  (3,4,2)
c = np.transpose(a, (1, 2, 0))
print(c, c.shape)
