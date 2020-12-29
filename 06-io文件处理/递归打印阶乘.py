# coding=utf-8

# 使用递归计算n的阶乘(5!=5*4*3*2*1)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))
