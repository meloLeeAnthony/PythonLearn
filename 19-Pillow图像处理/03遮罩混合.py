# coding=utf-8
'''
    图片遮罩混合
    composite(im1,im2,mask)函数，mask、im1和im2三幅图片的尺寸必须相同
'''
from PIL import Image

img1 = Image.open('images/blend1.jpg')
img2 = Image.open('images/blend2.jpg')
img2 = img2.resize(img1.size)
r, g, b = img2.split()
Image.composite(img2, img1, b).show()
