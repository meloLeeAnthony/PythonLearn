# 导入模块
import _thread
import time


def fun1():
    print('开始运行fun1')
    time.sleep(4)
    print('运行fun1结束')


def fun2():
    print('开始运行fun2')
    time.sleep(2)
    print('运行fun2结束')


if __name__ == '__main__':
    print('主线程开始运行')
    # 创建线程
    _thread.start_new_thread(fun1, ())
    _thread.start_new_thread(fun2, ())
    time.sleep(7)
    print('主线程运行结束')
