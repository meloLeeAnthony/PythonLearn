import time


# 可变参数：funcIn(*args, **kwargs)
def funcOut(func):
    def funcIn(*args, **kwargs):
        writeLog(func)
        return func(*args, **kwargs)

    return funcIn


def writeLog(func):
    print('访问方法名：', func.__name__, '\t时间:', time.asctime())


@funcOut
def sum(a, b):
    return a + b


@funcOut
def add(a, b, c):
    return a + b + c


result = sum(10, 20)
print('两个数的和：', result)
result = add(10, 20, 30)
print('三个数的和：', result)
