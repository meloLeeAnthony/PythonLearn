# 使用装饰器 完成不修改fun1() fun2()函数的源码，添加输出日志信息
#   装饰器就是一种闭包，它可以是闭包的访问方式更简单
import time
import traceback


def writeLog(func):
    try:
        file = open('log.txt', mode='a', encoding='utf-8')
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


# 使用闭包
def funcOut(func):
    def funcIn():
        writeLog(func)
        func()

    return funcIn


# 使用装饰器
@funcOut  # fun1=funcOut(fun1)
def fun1():
    print('功能1')


@funcOut  # fun2=funcOut(fun2)
def fun2():
    print('功能2')


# 装饰器的调用
fun1()
fun2()
