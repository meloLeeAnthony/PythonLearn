import threading

# 创建ThreadLocal对象
local = threading.local()


def process_student():
    student_name = local.name
    print('线程名：%s  学生姓名:%s' % (threading.current_thread().getName(), student_name))


def process_thread(name):
    # 将传入的name值绑定到local的name上
    local.name = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('张三',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('李四',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
