# coding=utf-8
'''
Created on 2018年10月9日

@author: Administrator
'''
a = "abcdefg123"
print(a[0])
print(a[-1])
print(a[0:3])
print(a[:3])
print(a[2:])
print(a[2:10])
print(a[0:4:3])
print(a[::-1])
print(a[1:-1])
print(a[6:0:-2])
print(a.find("a"))
b = "hello world hi python"
print(b.title())
print(a.rjust(20))
print(a.ljust(20))
print("*" * 50)
print(a.center(50))
print("*" * 50)
print(a.isalpha())
# print(a[10])
print(a[2:10])

print("-" * 50)
# 在创建字符串时，可以在字符串中指定占位符
# %s 在字符串中表示任意字符
# %f 浮点数占位符
# %d 整数占位符
c = 'Hello %s' % '孙悟空'
print(c)
c = 'hello %s 你好 %s' % ('tom', '孙悟空')
print(c)
c = 'hello %3.5s' % 'abcdefg'  # %3.5s字符串的长度限制在3-5之间
print(c)
c = 'hello %s' % 123.456
print(c)
c = 'hello %.2f' % 123.456
print(c)
c = 'hello %d' % 123.95
print(c)

print('a = %s' % a)

# 格式化字符串，可以通过在字符串前添加一个f来创建一个格式化字符串
# 在格式化字符串中可以直接嵌入变量
c = f'hello {a} {b}'
print(c)

print(f'a = {a}')
