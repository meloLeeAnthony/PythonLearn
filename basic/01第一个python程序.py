# coding=utf-8
# -*- coding:utf-8 -*-
"""
Created on 2018年10月9日

@author: lcl253137@alibaba-inc.com
"""
print("hello python")

num1 = 1
num2 = 2
print("%d+%d=%d" % (num1, num2, num1 + num2))
print("hello,%s" % "world")
print('The quick brown fox', 'jumps over', 'the lazy dog')

# 布尔值实际上也属于整型，True就相当于1，False就相当于0
print(1 + True)
print(True)
print(False)

a = "hello"
b = 'world'
c = '123'
d = int(c)
print(d)

d = (85 - 72) / 72 * 100
print(d)
print("%.1f%%" % d)

e = input("请输入数字：")
print(e)
print(10 // 3.0)
print(2 ** 3)
e = 10
e += 1
print(e)

result = 1 < 2 < 3  # 相当于 1 < 2 and 2 < 3
print(result)
