from PIL import Image, ImageFont, ImageDraw

img = Image.open('images/bjsxt.png')
print(img.size)
draw_obj = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw_obj.text((30, 10), 'bjsxt', font=font, fill='white')
font = ImageFont.truetype('C:\\Users\\lichu\\AppData\\Local\\Microsoft\\Windows\\Fonts\\华文行楷.ttf', 18)
draw_obj.text((30, 30), '北京尚学堂-1', font=font, fill='red')
font = ImageFont.truetype('C:\\Users\\lichu\\AppData\\Local\\Microsoft\\Windows\\Fonts\\华文行楷.ttf', 30)
draw_obj.text((30, 60), '北京尚学堂-2', font=font, fill='blue')
img.show()
