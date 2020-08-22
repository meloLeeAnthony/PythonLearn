from PIL import Image, ImageEnhance

# 打开图像
img = Image.open('images/blend1.jpg')
w, h = img.size
img_output = Image.new('RGB', (3 * w, h))
# 将原图复制到(0,0)
img_output.paste(img, (0, 0))
# 获取色彩调整器
img_color = ImageEnhance.Color(img)
imgb = img_color.enhance(1.5)
img_output.paste(imgb, (w, 0))
# 减弱色彩
imgc = img_color.enhance(0.5)
img_output.paste(imgc, (2 * w, 0))
img_output.show()
