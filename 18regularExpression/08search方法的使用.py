import re

pattern = 'hello'
s = 'hello python'
# m=re.search(pattern,s)
m = re.match(pattern, s)
print(m)
print(m.group())
print('-------macth和search的区别----------')
'''
    re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
    re.search 匹配整个字符串，直到找到一个匹配为止
'''
pattern = 'love'
s = 'I love you'
m = re.match(pattern, s)
print('使用match进行匹配', m)
o = re.search(pattern, s)
print('使用search进行匹配', o)
