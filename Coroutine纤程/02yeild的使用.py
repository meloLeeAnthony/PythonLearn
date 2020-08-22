def foo():
    print('starting')
    while True:
        res = yield 4
        print('res:', res)


'''
在函数中使用了yield，则该函数就成为了一个生成器
yield的理解
1.当成return程序返回
2.当成生成器
'''
g = foo()  # g就是一个生成器对象
print(type(g))
print(next(g))  # 第一次执行遇到yield就返回4，后面代码不执行
print('*' * 20)
print(next(g))  # 第二次执行在上次执行返回处继续执行，yield返回之后就为None
