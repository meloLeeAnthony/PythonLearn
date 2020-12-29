"""
通用装饰器
"""
import time


# 可变参数：funcIn(*args, **kwargs)
def funcOut(func):
    """
    闭包外层函数
    :param func: 传入闭包内层需要执行的参数
    :return: 闭包内层函数
    """
    def funcIn(*args, **kwargs):
        """
        闭包内层函数
        :param args: 可变参数 (元组)
        :param kwargs: 可变参数 (字典)
        :return: 传进来的参数执行后的返回结果
        """
        writeLog(func)
        return func(*args, **kwargs)

    return funcIn


def writeLog(func):
    """
    添加日志输出信息
    :param func: 真正执行的函数
    """
    print('访问方法名：', func.__name__, '\t时间:', time.asctime())


@funcOut
def sum(a, b):
    """
    计算两个数的和
    :param a: 参数a
    :param b: 参数b
    :return: 两个数的和
    """
    return a + b


@funcOut
def add(a, b, c):
    """
    计算三个数的和
    :param a: 参数a
    :param b: 参数b
    :param c: 参数c
    :return: 三个数的和
    """
    return a + b + c


result = sum(10, 20)
print('两个数的和：', result)
result = add(10, 20, 30)
print('三个数的和：', result)
