# 导入模块
from multiprocessing import Process


# 定义任务的函数
def run_test(name, age, **kwargs):
    print('子进程正在运行 name的值:%s ,age的值：%d' % (name, age))
    print('字典kwargs:', kwargs)


if __name__ == '__main__':
    print('主进程开始执行')
    # 创建子进程
    p = Process(target=run_test, args=('test', 23), kwargs={'key': 12})
    # 调用子进程
    p.start()
