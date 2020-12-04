"""
什么是高阶函数？
1.变量可以指向函数
2.函数名也是变量
"""

# coding=utf-8
import traceback  # 异常模块

# 变量可以指向函数
# 求-10的绝对值
print(abs(-10))
print(abs)
# abs()代表对函数的调用    abs是函数本身
f = abs  # f变量也是指向abs所指向的函数
# 是否可以通过该变量f来调用这个函数？
print(f(-10))
# 结论：变量f指向了abs函数本身

# 函数名也是变量
# 函数名其实就是指向函数的变量。对于abs()这个函数，我们可以把函数名abs看成是一个变量，它指向计算绝对值的函数

try:
    # abs = 10
    print(abs(-10))
except TypeError as e:
    traceback.print_exc()
    abs = f

# 实际中变量名命名是不能这样写的，是为了说明函数名也是一个变量

'''
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另外一个函数作为参数，这种函数就称为高阶函数
'''


def add(x, y, function):
    """
    函数的入参function为函数
    :param x:
    :param y:
    :param function:
    :return:
    """
    return function(x) + function(y)  # abs(-10)+abs(5)


print(add(-10, 5, abs))
