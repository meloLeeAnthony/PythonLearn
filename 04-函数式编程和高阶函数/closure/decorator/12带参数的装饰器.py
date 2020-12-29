"""
带参数的装饰器
"""
import time


def writeLog(func):
    """
    添加日志输出信息
    :param func: 真正执行的函数
    """
    print('访问了方法名：', func.__name__, '\t时间：', time.asctime())


def funOut(func):
    """
    闭包外层函数
    :param func: 传入闭包内层需要执行的参数
    :return: 闭包内层函数
    """

    def funIn(x, y):
        """
        闭包内层函数
        :param x: 参数x
        :param y: 参数y
        :return: 传进来的参数执行后的返回结果
        """
        writeLog(func)
        return func(x, y)

    return funIn


@funOut
def sum(a, b):
    """
    计算两个数的和
    :param a: 参数a
    :param b: 参数b
    :return: 两个数的和
    """
    return a + b


result = sum(10, 20)
print('两数的和：', result)


# 功能函数三个参数
def funOut2(func):
    """
    闭包外层函数
    :param func: 传入闭包内层需要执行的参数
    :return:
    """

    def funcIn(a, b, c):
        """
        计算三个数的和
        :param a: 参数a
        :param b: 参数b
        :param c: 参数c
        :return: 三个数的和
        """
        writeLog(func)
        return func(a, b, c)

    return funcIn


@funOut2
def add(a, b, c):
    """
    计算三个数的和
    :param a: 参数a
    :param b: 参数b
    :param c: 参数c
    :return: 三个数的和
    """
    return a + b + c


result = add(10, 20, 30)
print('三个数的和：', result)
