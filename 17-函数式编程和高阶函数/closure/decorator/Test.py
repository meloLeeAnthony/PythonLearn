def sum(a, b):
    return a + b


def sum1():
    return 3 + 5


def mul(a, b):
    return a * b


def printLog(func):
    def printLogImpl(a, b):
        print("开始计算")
        result = func(a, b)
        print('计算结束，结果为: %d' % result)

    return printLogImpl


printLog(sum)(2, 3)


@printLog
def mul1(a, b):
    return a * b


mul1(2, 3)
