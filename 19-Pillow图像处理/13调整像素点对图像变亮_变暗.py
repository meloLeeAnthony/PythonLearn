from PIL import Image

img = Image.open('images/blend1.jpg')
w, h = img.size
img_output = Image.new('RGB', (3 * w, h))
img_output.paste(img, (0, 0))
# 使用point()函数对像素点进行运算
# 图像整体变亮
imgb = img.point(lambda i: i * 1.5)
# 图像整体变暗
imgc = img.point(lambda i: i * 0.5)
img_output.paste(imgb, (w, 0))
img_output.paste(imgc, (2 * w, 0))
img_output.show()
