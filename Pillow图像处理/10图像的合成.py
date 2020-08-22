from PIL import Image, ImageChops

# 打开图片
img1 = Image.open('images/blend1.jpg')
img2 = Image.open('images/blend2.jpg')
# 对两张图片进行算术加法运算
ImageChops.add(img1, img2).show()

# 对两张图片进行算术减法运算
ImageChops.subtract(img1, img2).show()

# darker函数：比较两个图片的像素，取两张图片中对应像素的较小值，所以合成时两幅图像中对应位置的暗部分得到保留，而去除亮部分
ImageChops.darker(img1, img2).show()

# lighter变亮函数：与darker变暗函数相反，功能是比较两个图片（逐像素比较），返回一幅新的图片，这幅新的图片是将两张图片中较亮的部分叠加得到的
ImageChops.lighter(img1, img2).show()

# multiply叠加函数:将两张图片互相叠加
ImageChops.multiply(img1, img2).show()

# sreen函数:先反色后叠加，实现合成图像的效果
ImageChops.screen(img1, img2).show()

# invert反色函数:类似于集合操作中的求补集，最大值为Max，每个像素做减法，取出反色
ImageChops.invert(img1).show()

# difference比较函数:可以逐像素做减法操作，计算出绝对值
ImageChops.difference(img2, img2).show()
