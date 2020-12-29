"""
Created on 2018年10月10日

@author: Administrator
"""


class Person(object):
    """
    面向对象的对象: 人
    """
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def setName(self, name):
        """
        面向对象的方法: 设置姓名
        :param name:
        """
        if len(name) > 5:
            self.__name = name
        else:
            print("名字长度不符合规则")

    def getName(self):
        """
        获取姓名
        :return:
        """
        return self.__name

    @staticmethod
    def __test():
        print("test")

    def test2(self):
        """
        包装方法
        """
        self.__test()


p = Person("abcdefg", 3)
# print(p.__name)
print(p.getName())
p.setName("abcd")
print(p.getName())
# p.__test()
p.test2()
