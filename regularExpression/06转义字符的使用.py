'''
    使用原生字符串r作为前缀，避免一堆\理不清的问题

    匹配一个数字的“\\d”可以写成r“\d”
'''
# coding=utf-8
import re

print('d:\\a\\b\\c')
print('\nabc')
print('\\nabc')
print('\t123')
print('\\t123')

s = '\\t123'
# pattern='\\\\t\d*'
pattern = r'\\t\d*'  # 使用原生字符串r作为前缀
o = re.match(pattern, s)
print(o)

s = '\\\\t123'
# pattern='\\\\\\\\t\d*'
pattern = r'\\\\t\d*'
o = re.match(pattern, s)
print(o)
