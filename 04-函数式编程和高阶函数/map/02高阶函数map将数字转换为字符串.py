"""
 map(func, *iterables) --> map 05-object面向对象

    Make an iterator that computes the 03-function函数 using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
"""
integ = 10
# 将10转换为字符串
integStr = str(integ)
print(type(integStr))
print(integStr + '\n')

integ = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 将列表中每个元素转换为字符串
ieters = map(str, integ)
print(type(ieters))
print(list(ieters))
