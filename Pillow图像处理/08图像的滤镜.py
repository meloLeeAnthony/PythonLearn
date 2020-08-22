from PIL import Image, ImageFilter

img = Image.open('images/lena.jpg')
w, h = img.size
# 创建一个图像
img_output = Image.new('RGB', (2 * w, h))
img_output.paste(img, (0, 0))
img_filter = img.filter(ImageFilter.GaussianBlur)
img_output.paste(img_filter, (w, 0))
img_output.show()
