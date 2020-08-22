# coding=utf-8
from PIL import Image, ImageDraw, ImageFont

# 创建一幅白色背景的图像
img = Image.new('RGB', (500, 500), 'white')

# 绘制一个矩形
draw_obj = ImageDraw.Draw(img)
draw_obj.rectangle((50, 50, 350, 300), fill='white', outline='red')
draw_obj.text((80, 80), 'bjsxt', fill='green')

# UnicodeEncodeError: 'latin-1' codec can't encode character '\u554a' in position 6: ordinal not in range(256)
# 字体文件夹在C:\Windows\Fonts目录下
font = ImageFont.truetype("C:\\Users\\lichu\\AppData\\Local\\Microsoft\\Windows\\Fonts\\华文行楷.ttf", 40, encoding="uft-8")  # 设置字体
draw_obj.text((80, 160), '北京尚学堂', font=font, fill='green')
img.show()
