# 导入numpy模块
import numpy as np

# 创建一维数组
a = np.arange(10)
print(a)
# 正索引访问  索引从0开始  长度-1
print('索引0处的元素：', a[0])
print('索引5处的元素：', a[5])

# 负索引访问  倒数第一个的索引为-1
print('访问最后一个元素：', a[-1])
print('访问倒数第三个元素：', a[-3])

# 切片正向索引操作  [start:stop:step]
print(a[:])  # 从开始到结尾
print(a[3:])  # 从索引3开始到结尾
print(a[3:5])  # 从索引3开始到索引4 [start,stop)结尾
print(a[1:7:2])  # 从索引1开始到索引6，步长是2

# 切片中负索引操作
print(a[::-1])  # 反向获取
print(a[-5:-2])
