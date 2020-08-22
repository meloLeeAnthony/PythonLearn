from PIL import Image

image = Image.open('images/lena.jpg')
print('原来图片的形状', image.size)
image.show()

# copy()：图片拷贝
# resize_img = image.copy()
resize_img = image.copy().resize((600, 560))
# size返回的是图像的宽度：600，高度：560
print('修改后图片的形状：', resize_img.size)
resize_img.show()
