import time


def writeLog(func):
    print('访问了方法名：', func.__name__, '\t时间：', time.asctime())


def funOut(func):
    def funIn(x, y):
        writeLog(func)
        return func(x, y)

    return funIn


@funOut
def sum(a, b):
    return a + b


result = sum(10, 20)
print('两数的和：', result)


# 功能函数三个参数
def funOut2(func):
    def funcIn(a, b, c):
        writeLog(func)
        return func(a, b, c)

    return funcIn


@funOut2
def add(a, b, c):
    return a + b + c


result = add(10, 20, 30)
print('三个数的和：', result)
