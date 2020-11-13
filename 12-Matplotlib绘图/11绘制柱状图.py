# 导入模块
import matplotlib.pyplot as plt

# 创建x ，y  表示x年份  y表示年份对应的销量
x = [1980, 1985, 1990, 1995]
x_label = ['1980年', '1985年', '1990年', '1995年']
y = [1000, 3000, 4000, 5000]
# 调用bar函数绘制柱状图
plt.bar(x, y, width=3, facecolor='yellowgreen', edgecolor='white')  # width修改柱的宽度
# 修改中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 修改x坐标的值
plt.xticks(x, x_label)
# 给x坐标y坐标添加名称
plt.xlabel('年份')
plt.ylabel('销量')
# 添加标题title
plt.title('根据年份销量对比图')
plt.show()
