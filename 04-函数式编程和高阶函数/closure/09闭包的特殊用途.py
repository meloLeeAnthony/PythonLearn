"""
闭包的特殊用途：不修改源代码的前提下，添加新的功能
添加日志输出信息
"""
import time
import traceback


def writeLog(func):
    """
    添加日志输出信息
    :param func: 需要执行的函数
    """
    try:
        file = open('writeLog.txt', mode='a', encoding='utf-8')
        # 向文件中写入日志信息
        file.write('访问：')
        file.write(func.__name__)
        file.write('\t')
        file.write('时间：')
        file.write(time.asctime())
        file.write('\n')
    except Exception as e:
        traceback.print_exc()
    finally:
        file.close()


def fun1():
    """
    不符合开闭原则
    """
    # writeLog(fun1)
    print('功能1')


def fun2():
    """
    不符合开闭原则
    """
    # writeLog(fun2)
    print('功能2')


# 使用闭包，不修改fun1  和fun2的功能代码，添加日志信息，类似于Spring AOP切面编程的功能
def funcOut(func):
    """
    使用闭包，不修改fun1  和fun2的功能代码，添加日志信息，类似于Spring AOP切面编程的功能
    :param func: 需要执行的函数
    :return: AOP切面函数
    """
    def funcIn():
        """
        添加日志输出信息
        """
        writeLog(func)
        func()
        print('调用', func.__name__, '结束')

    return funcIn


fun1 = funcOut(fun1)
fun1()
fun2 = funcOut(fun2)
fun2()
