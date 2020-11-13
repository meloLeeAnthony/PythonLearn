# 导入numpy
import numpy as np

# 创建两个数组
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[11, 12, 13], [14, 15, 16]])
print(a)
print(b)
# 使用hstack进行水平拼接
# r=np.hstack([a,b])
r = np.hstack((a, b))
print(r)

# 使用vstack进行垂直方向拼接
r = np.vstack((a, b))
print(r)

# concatenate的使用
print('axis=0 默认情况  垂直方向拼接  相当于vstack')
r1 = np.concatenate((a, b), axis=0)
r2 = np.concatenate((a, b))
print(r1)
print(r2)

# 二维数组有两个轴 axis=0   axis=1
print('axis=1   水平方向拼接  相当于hstack')
r3 = np.concatenate((a, b), axis=1)
print(r3)

# 三维数组有三个轴  axis=0 1 2
a = np.arange(1, 13).reshape(1, 2, 6)
print(a, a.shape)
b = np.arange(101, 113).reshape(1, 2, 6)
print(b, b.shape)
print('三维 axis=0')
r1 = np.concatenate((a, b), axis=0)
print(r1, r1.shape)

print('三维 axis=1')
r2 = np.concatenate((a, b), axis=1)
print(r2, r2.shape)

print('三维 axis=2')
r3 = np.concatenate((a, b), axis=2)
print(r3, r3.shape)
