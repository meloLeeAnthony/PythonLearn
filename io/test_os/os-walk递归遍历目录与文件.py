# coding=utf-8
# 测试os.walk()递归遍历所有的子目录和子文件

import os

all_files = []
path = os.getcwd()
list_files = os.walk(path)

for dirpath, dirnames, filenames in list_files:
    for dir in dirnames:
        all_files.append(os.path.join(dirpath, dir))
        print("1:" + dirpath)
        print(dir)
    for file in filenames:
        all_files.append(os.path.join(dirpath, file))
        print("2:" + dirpath)
        print(file)

# 打印所有的子目录和子文件
for file in all_files:
    print(file)
