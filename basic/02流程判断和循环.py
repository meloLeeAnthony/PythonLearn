# coding=utf-8
"""
Created on 2018年10月9日

@author: Administrator
"""
age = input("请输入年龄：")
age = int(age)
if age > 20:
    print("长大了")
elif age > 40:
    print("老了")
else:
    print("还小呢")

a = 10
if a > 10:
    pass
else:
    pass

i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)

# 九九乘法表
n = 1
while n < 10:
    c = 1
    while c <= n:
        print("%d*%d=%d" % (c, n, c * n), end="\t")
        if c == n:
            print()
        c += 1
    n += 1

total = 0
for i in range(1, 101):
    total += i
print(total)

for j in "abcdefg":
    print(j)
