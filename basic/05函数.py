"""
    Created on 2018年10月9日
    函数示例
@author: Administrator
"""


def test():
    """
        简单打印
    """
    print("python真简单")


test()


def add(paramA, paramB):
    """
        加法方法
    :param paramA: 参数a
    :param paramB: 参数b
    """
    print(paramA + paramB)


add(1, 2)


def add2(paramA, paramB=2):
    """
        加法方法
    :param paramA: 参数a
    :param paramB: 参数b，默认值为2
    """
    print(paramA + paramB)


add2(1)


def function(paramA, paramB, *args, **kwargs):
    """
        可变参数的函数
    :param paramA: 参数a
    :param paramB: 参数b
    :param args: 将多个参数收集到一个“元组”对象中，存放所有未命名的变量参数
    :param kwargs: 将多个参数收集到一个“字典”对象中，存放所有命名参数
    """
    print(paramA)
    print(paramB)
    print(*args)
    for i in kwargs.items():
        print(i)


function(1, 2, 3, 4, 5, 6, 7, 8, m=7, x=9, y=10)


def add3(objectParam):
    """
        测试形参是对象的方法
    :param objectParam: 对象形参
    """
    objectParam += objectParam


# a = 10
# a = [1, 2]
a = (1, 2)
add3(a)
print(a)


def func(paramA, paramB):
    """
        测试函数作为入参
    :param paramA: 参数a
    :param paramB: 参数b
    :return:
    """
    returnC = paramA + paramB
    return returnC


print(func(2, 3))


def funUnpack(paramA, paramB, paramC):
    """
        参数的解包/拆包
    :param paramA: 参数a
    :param paramB: 参数b
    :param paramC: 参数c
    """
    print('paramA=', paramA)
    print('paramB=', paramB)
    print('paramC=', paramC)


t = (10, 20, 30)
funUnpack(*t)
d = {'paramA': 10, 'paramB': 20, 'paramC': 30}
funUnpack(**d)


def func2(a):
    b = 100 + a
    c = 200 + a
    return b, c


b, c = func2(200)
print(b)
print(c)

a = 10


def func():
    global a
    a = a + 10
    print(a)


func()
print(a)
a = 100
print(id(a))


def test1():
    a = 10
    print(a)
    a = 20
    print(a)


def test2():
    global a
    a += 100
    print(a)
    print(id(a))


# test1()
test2()
print(a)
print(id(a))

b = 10


def test():
    c = b
    print(b)
    print(c)


test()


def createNum(a):
    arr = []

    def getNum(b):
        if b < 2:
            return 1
        else:
            return getNum(b - 1) + getNum(b - 2)

    for i in range(0, a):
        arr.append(getNum(i))
    print(arr)


createNum(20)

sum = lambda a, b, c: a + b + c
print(sum(1, 2, 3))


def test(a, b, opt):
    print(a)
    print(b)
    print("result:%d" % opt(a, b))


test(1, 2, lambda a, b: a + b)

stus = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}, {"name": "wangwu", "age": 17}]
stus.sort(key=lambda x: x["age"])
print(stus)
