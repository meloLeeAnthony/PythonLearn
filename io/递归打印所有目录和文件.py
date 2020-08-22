# coding=utf-8
# 递归打印所有的目录和文件

import os

allfiles = []


def getAllFiles(path, level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getAllFiles(filepath, level + 1)
        allfiles.append("\t" * level + filepath)


getAllFiles("test_os", 0)

for f in reversed(allfiles):
    print(f)
