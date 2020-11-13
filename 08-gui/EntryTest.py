"""测试Entry组件的基本用法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建登录界面的组件"""
        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        # StringVar变量绑定到指定的组件。
        # StringVar变量的值发生变化，组件内容也变化；
        # 组件内容发生变化，StringVar变量的值也发生变化。
        # StringVar与Entry双向绑定
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get())
        print(self.entry01.get())

        # 创建密码框
        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()

        Button(self, text="登陆", command=self.login).pack()

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()

        print("去数据库比对用户名和密码！")
        print("用户名："+username)
        print("密码："+pwd)

        if username == "gaoqi" and pwd == "123456":
            messagebox.showinfo("尚学堂学习系统", "登录成功！欢迎开始学习！")
        else:
            messagebox.showinfo("尚学堂学习系统", "登录失败！用户名或密码错误！")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x130+200+300")
    app = Application(master=root)
    root.mainloop()