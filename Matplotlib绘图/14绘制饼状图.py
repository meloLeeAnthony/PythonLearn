# 导入模块
import matplotlib.pyplot as plt

# 准备男、女的人数及比例
man = 71351
woman = 68187
man_perc = man / (woman + man)
woman_perc = woman / (woman + man)
# 添加名称
labels = ['男', '女']
# 添加颜色
colors = ['blue', 'red']

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

# 绘制饼状图  pie
# labels 名称 colors：颜色，explode=分裂  autopct显示百分比
paches, texts, autotexts = plt.pie([man_perc, woman_perc], labels=labels, colors=colors, explode=(0, 0.05),
                                   autopct='%0.1f%%')

# 设置饼状图中的字体颜色
for text in autotexts:
    text.set_color('white')

# 设置字体大小
for text in texts + autotexts:
    text.set_fontsize(20)

plt.show()
