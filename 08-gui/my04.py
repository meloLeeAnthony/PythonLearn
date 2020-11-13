"""测试Button组件的基本用法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(root, text="登录", width=6, height=3, anchor=NE, command=self.login)
        self.btn01.pack()

        global photo
        photo = PhotoImage(file="imgs/start.gif")
        self.btn02 = Button(root, image=photo, command=self.login)
        self.btn02.pack()
        self.btn02.config(state="disabled")  # 设置按钮为禁用

    def login(self):
        messagebox.showinfo("尚学堂学习系统", "登录成功！欢迎开始学习！")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x130+200+300")
    app = Application(master=root)
    root.mainloop()
