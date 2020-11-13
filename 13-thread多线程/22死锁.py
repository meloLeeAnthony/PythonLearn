import time
from threading import Thread, Lock

# 创建互斥锁
lock_a = Lock()
lock_b = Lock()


class MyThread1(Thread):
    def run(self):
        if lock_a.acquire():
            print(self.name, '执行')
            time.sleep(1)
            if lock_b.acquire():
                print(self.name, '执行')
                time.sleep(1)
                lock_b.release()
            lock_a.release()


class MyThread2(Thread):
    def run(self):
        if lock_b.acquire():
            print(self.name, '执行')
            time.sleep(1)
            if lock_a.acquire():
                print(self.name, '执行')
                time.sleep(1)
                lock_a.release()
            lock_b.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
