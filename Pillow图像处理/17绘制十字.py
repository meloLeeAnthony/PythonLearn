from PIL import Image, ImageDraw

img = Image.open('images/blend1.jpg')
draw_obj = ImageDraw.Draw(img)
w, h = img.size
# 255, 255, 0:»ÆÉ«£» 255, 0, 0£ººìÉ«
draw_obj.line((0, 0, w, h), fill=(255, 255, 0), width=3)
draw_obj.line((0, h, w, 0), fill=(255, 0, 0), width=3)
img.show()
