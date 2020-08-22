# coding=utf-8
'''
    图片透明度混合
    blend函数，im1和im2这两幅图片尺寸必须相同
'''
from PIL import Image

img1 = Image.open('images/bjsxt.png').convert(mode='RGB')
img2 = Image.new('RGB', img1.size, 'red')
# 混合两幅图
Image.blend(img1, img2, alpha=0.5).show()
