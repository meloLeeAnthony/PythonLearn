# 给foo函数，新增功能
# 在调用foo函数前，输出 ’I am foo‘
def funOut(func):
    print('装饰器1')

    def funIn():
        print('I am foo')
        func()

    return funIn


def funOut2(func):
    print('装饰器2')

    def funIn():
        print('hello')
        func()

    return funIn

@funOut2  # foo=funOut2(funcOut(foo))
@funOut  # foo=funcOut(foo)
def foo():
    print('foo函数正在运行')


# 使用闭包调用
# foo=funOut(foo)
foo()
