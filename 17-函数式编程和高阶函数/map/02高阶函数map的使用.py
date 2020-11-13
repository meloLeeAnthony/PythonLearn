'''
* DeprecationWarning:
* Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated,
* and in 3.8 it will stop working
*   from collections import Iterator
'''
from collections.abc import Iterator

'''
 map(func, *iterables) --> map 04-object面向对象

    Make an iterator that computes the 03-function函数 using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
'''
# 一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]
arrs = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func(x):
    return x * x


result_list = []
for i in arrs:
    result_list.append(func(i))
print(result_list)

# 使用map实现
iters = map(func, arrs)  # 返回的it是一个可迭代的对象
print(type(iters))
# 判断是否是可迭代的对象
print('判断是否可迭代：', isinstance(iters, Iterator))
print(list(iters))
