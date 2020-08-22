'''
    ImageDraw:pillow库的绘图对象
'''
from PIL import Image, ImageDraw

img = Image.open('images/lena.jpg')

draw_obj = ImageDraw.Draw(img)  # 创建绘图对象
draw_obj.rectangle((100, 100, 300, 300), outline='yellow', width=4)  # 绘制矩形(正方形)
draw_obj.ellipse((100, 100, 300, 300), outline='red', width=3)  # 绘制椭圆（圆形）
img.show()
