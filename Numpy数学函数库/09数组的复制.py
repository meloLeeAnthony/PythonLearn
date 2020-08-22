# 导入numpy模块
import numpy as np

# 创建一个二维的数组
a = np.arange(1, 13).reshape((3, 4))
print(a)
# 对a数组进行切片处理，获取第一、二行，第一二列
sub_a = a[:2, :2]
print(sub_a)
# 对sub_a中第一行第一列的值进行修改
# sub_a[0][0]=100
# print(sub_a)
# print(a)
# 通过切片可以获取到新数组，即使赋值给新的变量，但还是原来数组的视图。
# 如果对切片数组中元素的值，进行修改会影响原来的数组

# 可以使用numpy中的copy方法实现
sub_aa = np.copy(a[:2, :2])  # 是深拷贝
sub_aa[0, 0] = 200
print(sub_aa)
print(a)
