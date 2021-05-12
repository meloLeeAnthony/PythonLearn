# coding=utf-8
"""
Traceback追溯，追根溯源。most recent call last最后一次调用
ZeroDivisionError
"""

print("step0")
try:
    print("step1")
    a = 3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
    print(type(e))
print("end!!!!")
