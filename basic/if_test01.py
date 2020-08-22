num = input("输入一个数字：")
if int(num) < 10:
    print(num)
else:
    print("数字太大")

# 测试三元条件运算符
print(input("请输入一个数字") if int(num) < 10 else "数字太大")
