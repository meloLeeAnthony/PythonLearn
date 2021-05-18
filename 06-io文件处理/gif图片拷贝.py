"""
二进制文件读写
"""
with open("aa.gif", "rb") as f:
    with open("aa_copy.gif", "wb") as w:
        for line in f.readlines():
            w.write(line)

print("图片拷贝完成.........")
