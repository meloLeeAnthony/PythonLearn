# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 绘制20种大小 20种颜色的散点图
# 创建x
np.random.seed(0)  # 执行多次每次获取的随机数都是一样的
x = np.random.rand(20)
y = np.random.rand(20)
# 生成10种大小
size = np.random.rand(10) * 1000
# 生成20种颜色
color = np.random.rand(20)
print('x:', x)
print('y:', y)
print('color:', color)
# 绘制散点图
plt.scatter(x, y, s=size, c=color, alpha=0.7)  # s表示点的大小 c表示点的颜色 alpha表示透明度
plt.show()
'''
注意：点的个数和颜色的个数要相同
      点的个数和点大小的个数可以不同，如果点的个数大于大小的个数，则会循环获取大小
'''
