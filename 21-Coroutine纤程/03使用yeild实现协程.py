import time


def A():
    while True:
        print('-------A--------')
        yield
        time.sleep(0.5)


def B(c):
    while True:
        print('-------B--------')
        c.__next__()  # 返回迭代器的下一个元素
        time.sleep(0.5)


a = A()  # 生成一个生成器对象
B(a)
