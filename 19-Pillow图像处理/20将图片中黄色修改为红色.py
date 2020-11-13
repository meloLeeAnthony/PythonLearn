from PIL import ImageDraw, Image

img = Image.open('images/bjsxt.png')
draw_obj = ImageDraw.Draw(img)
width, height = img.size


# 将黄色修改为红色
def get_color(oldColor):
    '''
        如果是黄色(255,255,0)，则换算成红色,把绿色通道置为0
        可以点击：windows 中的画图软件调色板观察黄色的区间。
    '''
    # print(oldColor)
    # 获取每个通道的值  正宗的黄色(255,255,0)
    if oldColor[0] > 60 and oldColor[1] > 60:
        return (oldColor[0], 0, oldColor[2])  # 返回红色
    else:
        return oldColor


for x in range(width):
    for y in range(height):
        oldColor = img.getpixel((x, y))
        draw_obj.point((x, y), fill=get_color(oldColor))
# img.show()
img.save('images/bjsxt_red.jpg')
