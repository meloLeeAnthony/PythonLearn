# 导入模块
import threading
import time


def fun1(thread_name, delay):
    print('线程{}开始执行fun1'.format(thread_name))
    time.sleep(delay)
    print('线程{}运行fun1结束'.format(thread_name))


def fun2(thread_name, delay):
    print('线程{}开始执行fun2'.format(thread_name))
    time.sleep(delay)
    print('线程{}运行fun2结束'.format(thread_name))


if __name__ == '__main__':
    print('开始运行')
    # 创建线程
    t1 = threading.Thread(target=fun1, args=('14-thread多线程-1', 2))
    t2 = threading.Thread(target=fun2, args=('14-thread多线程-2', 3))
    # 启动线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()
