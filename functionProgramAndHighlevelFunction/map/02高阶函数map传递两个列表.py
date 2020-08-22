'''
 map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.

    Stops when the shortest iterable is exhausted.
'''
a = [1, 2, 3, 4]
b = [10, 20, 30]


def func(x, y):
    return x + y


ieters = map(func, a, b)
print(type(ieters))
print(list(ieters))
