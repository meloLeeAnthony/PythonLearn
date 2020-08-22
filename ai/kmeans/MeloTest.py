# -*- coding: UTF-8 -*-
# K-means Algorithm is a clustering algorithm
import random

import matplotlib.pyplot as plt
import numpy as np


def get_distance(p1, p2):
    diff = [x - y for x, y in zip(p1, p2)]
    distance = np.sqrt(sum(map(lambda x: x ** 2, diff)))
    return distance


# 计算多个点的中心
# cluster = [[1,2,3], [-2,1,2], [9, 0 ,4], [2,10,4]]
def calc_center_point(cluster):
    N = len(cluster)
    m = np.matrix(cluster).transpose().tolist()
    center_point = [sum(x) / N for x in m]
    return center_point


# 检查两个点是否有差别
def check_center_diff(center, new_center):
    n = len(center)
    for c, nc in zip(center, new_center):
        if c != nc:
            return False
    return True


# K-means算法的实现
def K_means(points, center_points):
    N = len(points)  # 样本个数
    n = len(points[0])  # 单个样本的维度
    k = len(center_points)  # k值大小

    tot = 0
    while True:  # 迭代
        temp_center_points = []  # 记录中心点

        clusters = []  # 记录聚类的结果
        for c in range(0, k):
            clusters.append([])  # 初始化

        # 针对每个点，寻找距离其最近的中心点（寻找组织）
        for i, data in enumerate(points):
            distances = []
            for center_point in center_points:
                distances.append(get_distance(data, center_point))
            index = distances.index(min(distances))  # 找到最小的距离的那个中心点的索引，

            clusters[index].append(data)  # 那么这个中心点代表的簇，里面增加一个样本

        tot += 1
        print(tot, '次迭代   ', clusters)
        k = len(clusters)
        colors = ['r.', 'g.', 'b.', 'k.', 'y.']  # 颜色和点的样式
        for i, cluster in enumerate(clusters):
            data = np.array(cluster)
            data_x = [x[0] for x in data]
            data_y = [x[1] for x in data]
            plt.subplot(2, 3, tot)
            plt.plot(data_x, data_y, colors[i])
            plt.axis([0, 1000, 0, 1000])

        # 重新计算中心点（该步骤可以与下面判断中心点是否发生变化这个步骤，调换顺序）
        for cluster in clusters:
            temp_center_points.append(calc_center_point(cluster))

        # 在计算中心点的时候，需要将原来的中心点算进去
        for j in range(0, k):
            if len(clusters[j]) == 0:
                temp_center_points[j] = center_points[j]

        # 判断中心点是否发生变化：即，判断聚类前后样本的类别是否发生变化
        for c, nc in zip(center_points, temp_center_points):
            if not check_center_diff(c, nc):
                center_points = temp_center_points[:]  # 复制一份
                break
        else:  # 如果没有变化，那么退出迭代，聚类结束
            break

    plt.show()
    return clusters  # 返回聚类的结果


# 随机获取一个样本集，用于测试K-means算法
def get_test_data():
    N = 1000

    # 产生点的区域
    area_1 = [0, N / 4, N / 4, N / 2]
    area_2 = [N / 2, 3 * N / 4, 0, N / 4]
    area_3 = [N / 4, N / 2, N / 2, 3 * N / 4]
    area_4 = [3 * N / 4, N, 3 * N / 4, N]
    area_5 = [3 * N / 4, N, N / 4, N / 2]

    areas = [area_1, area_2, area_3, area_4, area_5]
    k = len(areas)

    # 在各个区域内，随机产生一些点
    points = []
    for area in areas:
        rnd_num_of_points = random.randint(50, 200)
        for r in range(0, rnd_num_of_points):
            rnd_add = random.randint(0, 100)
            rnd_x = random.randint(area[0] + rnd_add, area[1] - rnd_add)
            rnd_y = random.randint(area[2], area[3] - rnd_add)
            points.append([rnd_x, rnd_y])

    # 自定义中心点，目标聚类个数为5，因此选定5个中心点
    center_points = [[0, 250], [500, 500], [500, 250], [500, 250], [500, 750]]

    return points, center_points


if __name__ == '__main__':
    points, center_points = get_test_data()
    clusters = K_means(points, center_points)
    print('#######最终结果##########')
    for i, cluster in enumerate(clusters):
        print('cluster ', i, ' ', cluster)
