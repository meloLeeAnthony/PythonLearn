# coding=utf-8
# 导入numpy
import numpy as np

a = np.arange(9).reshape(3, 3)
b = np.array([10, 10, 10])
print('加法')
print(np.add(a, b))
print(a + b)
print('减法')
print(np.subtract(b, a))
print(b - a)

# out参数的使用
y = np.empty((3, 3), dtype=np.int)
np.multiply(a, 10, out=y)
print(y)

# 三角函数
a = np.array([0, 30, 60, 90])
print(np.sin(a))

# around ceil floor
a = np.array([1.0, 4.55, 123, 0.567, 25.332])
print('around:', np.around(a))
print('ceil:', np.ceil(a))
print('floor:', np.floor(a))

# 统计函数
a = np.arange(1, 13).reshape(3, 4)
print('原数组a')
print(a)
print('power:', np.power(a, 2))

# power中out的使用
x = np.arange(5)
y = np.zeros(10)
np.power(2, x, out=y[:5])
print(y)

#  median ()
# 一维数组的中位数
a = np.array([4, 3, 2, 5, 2, 1])  # 对数组排序 [1,2,2,3,4,5]  数组中元素个数为偶数 中位数指：中间两个数的平均值
print(np.median(a))

a = np.array([4, 3, 2, 5, 2])  # 对数组排序 [2,2,3,4,5]  数组中元素个数为奇数 中位数指：中间的数
print(np.median(a))

# 二维数组  要通过axis指定轴
a = np.arange(1, 13).reshape(3, 4)
print(a)
print('垂直方向 ', np.median(a, axis=0))
print('水平方向 ', np.median(a, axis=1))

# mean 求平均值
# 一维数组
a = np.array([4, 3, 2, 5, 2])
print(np.mean(a))
# 二维数组   axis指定轴求平均
a = np.arange(1, 13).reshape(3, 4)
print(a)
print('axis=0 垂直方向', np.mean(a, axis=0))
print('axis=1 水平方向', np.mean(a, axis=1))

# sum()  max()  min()
a = np.array([4, 3, 2, 5, 2])
print('max:', np.max(a))
print('sum:', np.sum(a))
print('min:', np.min(a))

# argmax argmin
print('argmin:', np.argmin(a))
print('argmax:', np.argmax(a))
