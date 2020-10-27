# coding=utf-8
"""
Created on 2018年10月9日

@author: Administrator
"""
a = ["a", "b", "c", 12, 12.34, "a", "v", "b", "a"]
print(a)
print(len(a))
print(a[-1])
print(a[::-1])

a.append("e")
print(a)
b = ["aa", "bb", "cc"]
a.extend("f")
a.extend(b)
b.extend(a)
print(a)
print(b)
a.insert(2, "hello")
print(a)
# del(a)
a.pop()
a.remove("hello")
print(a)

if "a" not in a:
    print("不存在")
else:
    print("存在")

# print(a.index("f",2,6))
print(a.count("a"))
# list存放  有序，不唯一的数据，数据类型不必一致
print(a)
c = [1, 3, 5, 2, 4]
print(c)
c.sort()
print(c)
c.sort(reverse=True)
print(c)
c.reverse()
print(c)

for item, chrs in enumerate(c):
    print("下标：%d----值：%s" % (item, chrs))

c[2] = "abcdefg"
print(c)

a = ("a", "c", "b")
b = (1, 2, 3, 4, 5)
print(id(a))
print(id(b))
# a[2]="d"
a = b
print(id(a))
print(a)
t = (1,)
print(t)

t = ("a", "b", ["A", "B"])
print(t)
# t[2][0]="X"
# t[2][1]="Y"
# y=["X","Y"]
# t[2]=y
print(t)
print(t.index("a", ))
print(t.count("a"))

# dict
person = {"aaa": 12, "bbb": 23, "ccc": 34}
print(person)
print(person["aaa"])
abc = {"a", "b", "c"}
print(abc)

# 通过dict()函数创建字典
person = dict(name="melo", age=23, gender="男")
print(person)

# 通过双值子序列创建字典
person = dict([("name", "melo"), ("age", 23), ("gender", "男")])
print(person)
print(len(person))
print("age" in person)

# key不存在则报错KeyError
# print(person["undefined"])

# key不存在则返回None，也可指定默认返回参数
print(person.get("undefined"))
print(person.get("undefined", "defaultParam"))

person["aaa"] = 100
print(person)
person["ddd"] = 200
print(person)
# 向字典中添加Key、value，存在不做任何操作，返回原值；不存在则添加该key
person.setdefault("ddd", 300)
print(person)
person.setdefault("eee", 400)
print(person)

# update()函数，将其他字典中的值添加到当前字典中,key重复则用后者value覆盖当前
teacher = {"a": 1, "b": 2}
student = {"x": 3, "a": 4}
teacher.update(student)
print(teacher)

del person["ddd"]
# del person
print(person)

# popitem()随机删除一个字典值，一般删除最后一个，返回删除的key-value元组
deleteItem = person.popitem()
print(person)
print("deleteItem=", deleteItem)

# pop()删除指定字典值
person.pop("aaa")
person.pop("undefined", "defaultParam")

# person.clear()
# print(person)

# copy()对字典进行浅复制，复制以后的对象和原对象之间独立
source = {"a", "b", "c"}
dest = source.copy()
print("source=", source, id(source))
print("dest=", dest, id(dest))

# 1、遍历key
for key in person.keys():
    print(key, person[key])
# 2、遍历value
for value in person.values():
    print(value)
# 3、遍历对象
for item in person.items():
    print(item)
# 4、遍历key, value
for key, value in person.items():
    print(key, value)

# set
# 使用{...}创建集合
s = {1, 2, 3, 4}
print(s, type(s))
ts = {(1, 2, 3), (2, 4)}
print(ts, type(ts))
# 使用set()创建集合
nulls = set()
print(nulls, type(nulls))
nns = set('melo')
print(nns, type(nns))
