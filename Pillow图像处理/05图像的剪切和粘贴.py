from PIL import Image

img = Image.open('images/bjsxt.png')
# 复制
imgb = img.copy()
imgc = img.copy()
# 剪切
img_crop = imgb.crop((10, 10, 120, 120))
# 粘贴
imgc.paste(img_crop, (30, 30))
imgc.show()
