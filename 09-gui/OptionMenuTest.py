"""OptionMenu的使用测试"""


from tkinter import *

root = Tk()
root.geometry("200x100")

v = StringVar(root)
v.set("百战程序员")
om = OptionMenu(root, v, "尚学堂", "百战程序员", "卓越班[保底18万]")

om["width"] = 10
om.pack()


def test1():
    print("最喜爱的机构:", v.get())
#    v.set("尚学堂")       # 直接修改了optionmenu中选中的值


Button(root, text="确定", command=test1).pack()

root.mainloop()
