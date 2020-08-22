class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
print(C.__mro__)

obj = object()
print(dir(obj))

