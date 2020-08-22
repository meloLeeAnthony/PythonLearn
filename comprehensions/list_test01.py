#  列表推导式
cells = [(row, col) for row in range(1, 10) for col in range(1, 10)]  # 可以使用两个循环
print(cells)
for cell in cells:
    print(cell)
