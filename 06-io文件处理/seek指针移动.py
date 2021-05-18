"""
seek移动指针读取
"""
with open("o.txt", encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())
    print("读取的内容：{0}".format(str(f.readline().strip('\n'))))
    print(f.tell())
    f.seek(0)
    print("读取的内容：{0}".format(str(f.readline().strip('\n'))))
    print(f.tell())
