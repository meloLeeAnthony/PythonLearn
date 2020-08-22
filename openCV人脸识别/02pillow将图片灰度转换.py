'''
    Pillow (Fork of the Python Imaging Library)
'''
from PIL import Image

image = Image.open('images/lena.jpg')
width, height = image.size

img_output = Image.new('RGB', (2 * width, height))
img_output.paste(image, (0, 0))

convertImg = image.convert("L")  # 转化为黑白图片
convertImg.save('images/pillow_lena_gray.jpg')
img_output.paste(convertImg, (width, 0))
img_output.show()
