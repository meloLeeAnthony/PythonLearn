# 闭包的特殊用途：不修改源代码的前提下，添加新的功能
# 添加日志输出信息
import time
import traceback


def writeLog(func):
    try:
        file = open('wirteLog.txt', mode='a', encoding='utf-8')
        # 向文件中写入日志信息（访问：方法名  时间：XXXX-XX-XX）
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

# 不符合开闭原则
def fun1():
    # writeLog(fun1)
    print('功能1')


def fun2():
    # writeLog(fun2)
    print('功能2')


# 使用闭包，不修改fun1  和fun2的功能代码，添加日志信息，类似于Spring AOP切面编程的功能
def funcOut(func):
    def funcIn():
        writeLog(func)
        func()
        print('调用', func.__name__, '结束')

    return funcIn


fun1 = funcOut(fun1)
fun1()
fun2 = funcOut(fun2)
fun2()
