from functools import reduce

# 计算一个序列的求和
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in a:
    sum += i
print('for循环累加求和：', sum)


def sumTest(x, y):
    return x + y


sum = reduce(sumTest, a)
print('reduce计算求和：', sum)
