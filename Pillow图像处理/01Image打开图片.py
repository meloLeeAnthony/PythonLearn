from PIL import Image

# 打开图片
img = Image.open('images/bjsxt.png')
# 显示图片
img.show()
print('图片的格式：', img.format)
print('图片的大小：', img.size)
print('图片的高度：', img.height, '; 图片的宽度：', img.width)
print('获取坐标为(100,100)处的像素值:', img.getpixel((100, 100)))
