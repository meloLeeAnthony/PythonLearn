import re

pattern = 'aa|bb|cc'  # |表示3个字符串至少匹配一个即可
s = 'aa'
o = re.match(pattern, s)
print(o)

s = 'bb'
o = re.match(pattern, s)
print(o)

s = 'my name is cc'
'''
    re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
    re.search 匹配整个字符串，直到找到一个匹配为止
'''
o = re.search(pattern, s)
o = re.match(pattern, s)
print(o)

print('匹配0-100之间所有的数字')
# 匹配0-100之间所有的数字  0-99|100
pattern = r'[1-9]?\d$|100$'
s = '1'
s = '11'
s = '99'
s = '100'
# s = '1000'
o = re.match(pattern, s)
print(o)
