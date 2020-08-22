# 给foo函数，新增功能
# 在调用foo函数前，输出 ’I am foo‘
def funOut(func):
    def funIn():
        print('I am foo')
        func()

    return funIn


@funOut
def foo():
    print('foo函数正在运行')


# 使用闭包调用
foo()  # foo=funOut(foo)
