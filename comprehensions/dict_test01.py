# 字典推导式
my_text = 'i love you, i love sxt, i love gaoqi'
char_count = {c: my_text.count(c) for c in my_text}
print(char_count)
