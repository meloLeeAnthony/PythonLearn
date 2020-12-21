"""
 map(func, *iterables) --> map 04-object面向对象

    Make an iterator that computes the 03-function函数 using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.

    Stops when the shortest iterable is exhausted.
"""
a = [1, 2, 3, 4]
b = [10, 20, 30]

ieters = map(lambda x, y: x + y, a, b)
print(type(ieters))
print(list(ieters))
