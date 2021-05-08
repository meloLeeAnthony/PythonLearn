"""
Created on 2018年10月10日

@author: Administrator
"""


class Person(object):
    """
    Person对象
    """
    # 类属性: 直接在类中定义的属性; 可以通过类或类的实例访问
    name = "zhangsan"

    #     def __init__(self, name,age):
    #         self.name=name
    #         self.age=age
    @classmethod
    def test(cls):
        """
        类方法: 第一个参数为cls，代表当前的类对象; 可以通过类或类的实例调用
        """
        print("类方法")

    def test2(self):
        """
        实例方法，第一个参数为self; 可以通过类或类的实例调用
        """
        print("test2")

    @staticmethod
    def test3():
        """
        静态方法: 只能通过类对象调用
        """
        print("test3")


# p = Person("lisi", 12)
p = Person()
print(p.name)
# 实例属性: 通过实例对象添加的属性，类对象无法访问
p.name = "wangwu"
print(p.name)
print(Person.name)
Person.name = "maliu"
print(Person.name)
print(p.name)

p = Person()
p.test()
p.test2()
p.test3()
Person.test()
# Person.test2()
Person.test3()
