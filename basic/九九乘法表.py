"""
打印9 * 9乘法表
"""
n = 1
while n < 10:
    c = 1
    while c <= n:
        print("%d*%d=%d" % (c, n, c * n), end="\t")
        if c == n:
            print()
        c += 1
    n += 1

for x in range(1, 10):
    for y in range(1, x + 1):
        print("{0} * {1} = {2}".format(x, y, x * y), end="\t")
    print()  # 仅用于换行
