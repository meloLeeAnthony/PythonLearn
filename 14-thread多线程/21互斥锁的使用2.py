from threading import Thread, Lock

num = 0
# 创建一个互斥锁
lock = Lock()


def test1():
    global num
    for i in range(100000):
        lock.acquire()  # 上锁
        num += 1
        lock.release()  # 释放锁
    print('执行test1函数num的值：{}'.format(num))


def test2():
    global num
    for i in range(100000):
        lock.acquire()  # 上锁
        num += 1
        lock.release()  # 释放锁
    print('执行test2函数num的值：{}'.format(num))


if __name__ == '__main__':
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
