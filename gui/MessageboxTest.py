"""通用消息框"""

from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.geometry("400x100")

a1 = showinfo(title="尚学堂", message="Python400集从零开始，深入底层，深入算法，打好基础。还手写神经网络")
print(a1)

root.mainloop()
