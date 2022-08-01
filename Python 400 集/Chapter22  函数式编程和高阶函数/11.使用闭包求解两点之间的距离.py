#使用闭包求解两点之间的距离
'''
    两个点 (x1,y1) (x2,y2)
    距离  math.sqrt((x1-x2)**2+(y1-y2)**2)
'''

#传统求解方法
import math
def getDis(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#求点(1,1)距离原点(0,0)的距离
result = getDis(1,1,0,0)
print(result)
#求点(2,2)距离原点(0,0)的距离
result = getDis(2,2,0,0)
print(result)

#使用闭包求解的方法
def getDisOut(x1,y1):
    def getDisIn(x2,y2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
    return getDisIn

#调用外部函数  方式①
getDisIn = getDisOut(0,0)
res = getDisIn(1,1)
print(res)

#调用外部函数  方式②
res = getDisOut(0,0)(1,1)
print(res)