from PIL import Image, ImageDraw

img = Image.open('images/lena.jpg')
width, height = img.size
# 创建绘图对象
draw_obj = ImageDraw.Draw(img)
draw_obj.arc((0, 0, width - 1, height - 1), 0, 360, fill='blue')
img.save('images/plusCircle.jpg')
img.show()