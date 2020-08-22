from PIL import Image

img = Image.open('images/bjsxt.png')
# 图像的旋转;    rotate函数返回此图像的副本
img.rotate(180).show()

# convert()
img_convert = img.convert('L')  # 转化为黑白图片
img_convert.show()

# 格式转换
img.transpose(Image.FLIP_TOP_BOTTOM).show()  # 上下滤镜
img.transpose(Image.FLIP_LEFT_RIGHT).show()  # 左右滤镜
img.transpose(Image.ROTATE_90).show()  # 90滤镜
img.transpose(Image.ROTATE_180).show()  # 180滤镜
img.transpose(Image.TRANSPOSE).show()  # 颠倒滤镜
