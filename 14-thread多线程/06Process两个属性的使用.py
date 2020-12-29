# 导入模块
import multiprocessing
import time


# 定义执行任务的函数
def colck(interval):
    for i in range(3):
        print('当前时间：{}'.format(time.ctime()))
        time.sleep(interval)


if __name__ == '__main__':
    # 创建子进程
    p = multiprocessing.Process(target=colck, args=(5,))
    p.start()
    print('p.pid:', p.pid)
    print('p.name:', p.name)
    print('p.is_alive:', p.is_alive())
    p.join()
