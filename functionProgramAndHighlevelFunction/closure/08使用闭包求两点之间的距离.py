# 使用闭包求两点之间的距离
'''
   两个点  (x1,y1)  (x2,y2)
   距离： math.sqrt((x1-x2)**2+(y1-y2)**2)
'''
import math


def getDis(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# 求点(1,1)距离原点(0,0)的距离
result = getDis(1, 1, 0, 0)
print('点(1,1)距离原点(0,0)的距离', result)

# 求点(2,2)距离原点(0,0)的距离
result = getDis(2, 2, 0, 0)
print('点(2,2)距离原点(0,0)的距离', result)


# 使用闭包求两点之间的距离
def getDisOut(x1, y1):
    def getDisIn(x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return getDisIn


# 求点(1,1)距离原点(0,0)的距离
# 调用外部函数
getDisIn = getDisOut(0, 0)
result = getDisIn(1, 1)
print('点(1,1)距离原点(0,0)的距离', result)

# 求点(2,2)距离原点(0,0)的距离
result = getDisIn(2, 2)
print('点(2,2)距离原点(0,0)的距离', result)
