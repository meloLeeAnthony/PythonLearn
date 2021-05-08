class Student:
    """
    Student类对象
    """
    def __init__(self, name, age):  # 构造方法第一个参数必须为self
        self.name = name  # 实例属性
        self.age = age

    def say_score(self):  # self必须位于第一个参数
        """
        类的实例属性打印
        """
        print("{0}的年龄是{1}".format(self.name, self.age))


s1 = Student("Melo", 30)  # s1是实例对象，自动调用__init__()方法
s1.say_score()

s1.salary = 10000

print(s1.salary)
