from PIL import Image, ImageFilter

img = Image.open('images/lena.jpg')
w, h = img.size
# 创建一个图像
img_output = Image.new('RGB', (4 * w, h))
img_output.paste(img, (0, 0))

img_filter1 = img.filter(ImageFilter.GaussianBlur)  # 高斯滤镜
img_output.paste(img_filter1, (w, 0))
img_filter2 = img.filter(ImageFilter.EDGE_ENHANCE)  # 边缘增强滤镜
img_output.paste(img_filter2, (2 * w, 0))
img_filter3 = img.filter(ImageFilter.FIND_EDGES)  # 寻找边缘滤镜
img_output.paste(img_filter3, (3 * w, 0))

img_output.show()
