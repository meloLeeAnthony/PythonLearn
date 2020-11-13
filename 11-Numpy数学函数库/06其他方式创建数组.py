# 导入numpy模块
import numpy as np


# zeros
def zerosTest():
    a = np.zeros(5)
    print(a)
    # 指定类型
    b = np.zeros((5,), dtype=int)
    print(b)
    # 创建二维数组
    c = np.zeros((3, 4))
    print(c)


# ones
def onesTest():
    a = np.ones(10)
    print(a)
    b = np.ones((2, 5), dtype=int)
    print(b)


# empty
def emptyTest():
    a = np.empty(8)
    print(a)

    b = np.empty((3, 4))
    print(b)


# linspace：用于创建一维等差数列数组
def linespaceTest():
    a = np.linspace(1, 10, 10, dtype=np.int)
    print(a)

    b = np.linspace(5, 20, 5, endpoint=False)
    print(b)


# logspace：用于创建等比数组
def logspaceTest():
    a = np.logspace(0, 9, 10, base=2)
    print(a)


# zerosTest()
# onesTest()
# emptyTest()
# linespaceTest()
logspaceTest()
