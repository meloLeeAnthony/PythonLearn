class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
print(C.__mro__)
# 获取当前类的所有直接父类
print(C.__bases__)

obj = object()
print(dir(obj))
