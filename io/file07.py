with open("i.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines = [item.rstrip() + " #" + str(index + 1) + "\n" for index, item in enumerate(lines)]  # 推导式生成列表
    print(enumerate(lines))
    print(list(enumerate(lines)))

with open("o.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
