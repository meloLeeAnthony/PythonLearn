'''
Created on 2018年10月10日

@author: Administrator
'''
for i in range(1, 10):
    print(i, end="\t")
print()

a = [i for i in range(1, 10)]
print(a)
a = [i * 2 for i in range(1, 10)]
print(a)
a = [i for i in range(1, 10) if i % 2 == 0]
print(a)

b = [(i, j, k) for i in range(1, 10) for j in range(1, 10) for k in range(1, 10)]
print(b)
c = (i for i in range(1, 10))
# print(c[1])
for tupleC in tuple(c):
    print(tupleC, end="\t")
print()

d = (1, 2, 3)
print(d[1])
