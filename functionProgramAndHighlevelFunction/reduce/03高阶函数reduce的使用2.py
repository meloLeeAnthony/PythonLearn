from functools import reduce

# 把序列[1, 3, 5, 7, 9]变换成整数13579。将列表中的每个元素乘以10加上后一个元素。
a = [1, 3, 5, 7, 9]


def fun(x, y):
    return x * 10 + y


result = reduce(fun, a)
print(result)
