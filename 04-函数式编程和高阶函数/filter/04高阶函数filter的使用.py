def is_odd(n):
    """
    在一个列表中，删掉偶数，保留奇数
    :param n: 传入参数
    :return: 校验结果
    """
    # if n%2==0:
    #     return False
    # else:
    #     return True
    return n % 2 == 1


L = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(L))

a = ['A', '', 'B', None, 'C', '  ']


def not_empty(s):
    """
    过滤序列中的空字符串
    :param s:
    :return:
    """
    return s and s.strip()


L = filter(not_empty, a)
print(type(L), ' ' * 5, list(L))
