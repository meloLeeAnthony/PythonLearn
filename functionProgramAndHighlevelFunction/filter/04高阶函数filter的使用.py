# 在一个列表中，删掉偶数，保留奇数
def is_odd(n):
    # if n%2==0:
    #     return False
    # else:
    #     return True
    return n % 2 == 1


L = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(L))

# 一个序列中的空字符串删掉
a = ['A', '', 'B', None, 'C', '  ']


def not_empty(s):
    return s and s.strip()


L = filter(not_empty, a)
print(list(L))
