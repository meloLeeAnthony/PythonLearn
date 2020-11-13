from PIL import Image, ImageEnhance

# 打开图像
img = Image.open('images/blend1.jpg')
w, h = img.size
img_output = Image.new('RGB', (3 * w, h))
# 将原图复制到(0,0)
img_output.paste(img, (0, 0))
# 获取亮度调整器
img_bright = ImageEnhance.Brightness(img)
imgb = img_bright.enhance(1.5)
img_output.paste(imgb, (w, 0))
# 减弱亮度
imgc = img_bright.enhance(0.5)
img_output.paste(imgc, (2 * w, 0))
img_output.show()
