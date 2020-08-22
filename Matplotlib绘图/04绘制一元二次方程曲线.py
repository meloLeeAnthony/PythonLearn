# 导入matplotlib
from PIL import Image
import matplotlib.pyplot as plt

# 准备x  y
x = range(-100, 100)  # 200个点
y = [i ** 2 for i in x]
# 绘制一元二次方程曲线
plt.plot(x, y)
# 保存图片
plt.savefig('result')  # 默认的格式png
# plt.savefig('result.jpg')
# ValueError: Format 'jpg' is not supported (supported formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz)

Image.open('result.png').convert('RGB').save('result.jpg')
plt.show()

