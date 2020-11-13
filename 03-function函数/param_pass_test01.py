# 可变参数的传递
b = [10, 20]


def f2(m):
    '''可变参数的传递'''
    print("m:", id(m))  # b 和m 是同一个对象
    m.append(30)  # 由于m 是可变对象，不创建对象拷贝，直接修改这个对象


f2(b)
print("b:", id(b))
print(b)

help(f2)
