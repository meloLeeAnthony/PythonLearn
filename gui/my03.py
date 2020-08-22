"""测试Label组件的基本用法，使用面向对象的方式"""

from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        """创建组件"""
        self.label01 = Label(self, text="百战程序员", width=10, height=2, bg="black", fg="white")
        self.label01["text"] = "ccc"
        self.label01.config(fg="red", bg="green")

        self.label01.pack()

        self.label02 = Label(self, text="高淇老师", width=10, height=2, bg="blue", fg="white", font=("黑体", 30))
        self.label02.pack()

        # 显示图像
        global photo    # 把photo声明成全局变量。如果是局部变量，本方法执行完毕后，图像对象销毁，窗口显示不出图像。
        photo = PhotoImage(file="imgs/logo.gif")
        self.label03 = Label(self, image=photo)
        self.label03.pack()

        self.label04 = Label(self, text="北京尚学堂\n百战程序员\n老高好帅，就是做饭不行", borderwidth=5, relief="groove", justify="right")
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x260+200+300")
    app = Application(master=root)
    root.mainloop()
