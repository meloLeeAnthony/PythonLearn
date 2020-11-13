import re

s = 'hello python'
pattern = 'hello'

o = re.match(pattern, s)
print(o)
print(dir(o))
print(o.group())  # 返回匹配的字符串
print(o.span())
print(o.start())

print('flags参数使用')
pattern = 'Hello'
o = re.match(pattern, s, flags=re.I)  # re.I表示忽略大小写
print(o)
print(o.group())
