#冒泡排序  对列表进行升序排序
def bubble_sort(alist):
    #相邻两个元素进行比较，如果发现位置错误则进行交换
    n=len(alist)
    for k in range(n-1):
        for i in range(n-1-k):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

#如果传入的一个列表，则检测一轮，查看是否进行的交换，如果没有进行交换，说明列表就是有序列表，则直接退出循环
def bubble_sort2(alist):
    #相邻两个元素进行比较，如果发现位置错误则进行交换
    n=len(alist)
    for k in range(n-1):
        count=0
        for i in range(n-1-k):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count+=1
        #判断count的值是否等于0，如果等于0说明没有交换
        if count == 0:
            break

alist=[7,5,3,6,44,22,99,11]
print('原数组：')
print(alist)
bubble_sort(alist)
print('排序后数组：')
print(alist)

alist2=[3, 5, 6, 7, 11,3, 22, 44, 99]

bubble_sort2(alist2)
print('有序列表：')
print(alist2)
