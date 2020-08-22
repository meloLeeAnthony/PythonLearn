# coding=utf-8
from PIL import Image, ImageDraw

width, height = 300, 300
img = Image.new('RGB', (width, height), (255, 255, 255))
draw_obj = ImageDraw.Draw(img)


def get_color(x, y):
    a = x // 100 + y // 100
    if a == 0:
        return (255, 0, 0)  # 红色
    elif a == 1:
        return (255, 255, 0)  # 黄色
    elif a == 2:
        return (0, 0, 0)  # 黑色
    elif a == 3:
        return (0, 0, 255)  # 蓝色
    elif a == 4:
        return (0, 255, 255)  # 青色
    else:
        return (255, 255, 255)  # 白色


for x in range(width):
    for y in range(height):
        draw_obj.point((x, y), fill=get_color(x, y))
img.show()
