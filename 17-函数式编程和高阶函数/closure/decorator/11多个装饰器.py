"""
给foo函数，新增功能
在调用foo函数前，输出 ’I am foo‘
"""


def funOut(func):
    """
    闭包外层函数
    :param func: 提供给内层函数执行的函数
    :return:
    """
    print('装饰器1')

    def funIn():
        """
        闭包内层函数
        """
        print('I am foo')
        func()

    return funIn


def funOut2(func):
    """
    闭包外层函数
    :param func: 提供给内层函数执行的函数
    :return:
    """
    print('装饰器2')

    def funIn():
        """
        闭包内层函数
        """
        print('hello')
        func()

    return funIn


@funOut2  # foo=funOut2(funcOut(foo))
@funOut  # foo=funcOut(foo)
def foo():
    """
    foo函数体
    """
    print('foo函数正在运行')


# 使用闭包调用
# foo=funOut(foo)
foo()
