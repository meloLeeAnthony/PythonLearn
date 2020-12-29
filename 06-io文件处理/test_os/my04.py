# coding=utf-8
# 列出工作目录下所有的.py文件，并输出文件名

import os

path = os.getcwd()

file_list = os.listdir(path)  # 列出子目录、子文件
for filename in file_list:
    if filename.endswith("py"):
        print(filename, end="\t")

print()
file_list2 = [filename for filename in os.listdir(path) if filename.endswith("py")]
for f in file_list2:
    print(f, end="\t")
