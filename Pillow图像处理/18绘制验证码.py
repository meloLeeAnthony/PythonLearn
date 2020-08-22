import random

from PIL import Image, ImageDraw, ImageFont

width, height = 100, 100
img = Image.new('RGB', (width, height), (255, 255, 255))
# 获取draw_obj对象
draw_obj = ImageDraw.Draw(img)


# 生成随机的颜色(像素点)
def get_color():
    return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))


# 生成验证码的随机背景色
for x in range(width):
    for y in range(height):
        draw_obj.point((x, y), fill=get_color())


# 生成随机的字母
def get_char():
    return chr(random.randint(65, 97))


font = ImageFont.truetype('simsun.ttc', 36)
# 绘制随机字母
for i in range(4):
    draw_obj.text((10 + i * 20, 40), get_char(), font=font, fill=(255, 0, 0))

# 绘制干扰线
draw_obj.line((0, 0, 100, 100), fill='green', width=5)
img.show()
