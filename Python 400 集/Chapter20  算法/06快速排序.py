[54, 26, 93, 17, 77, 31, 44, 55, 20]  #升序排序

[17,                  20,       26, 31, 44, 54, 55, 77, 93]

#稳定性 [(20,2), 26,(20,1) , 17, 77, 31, 44, 55, ,93]  不稳定的

#基准数（第一个元素）54 （比54小的放在左边   比54大的放到右边）
#low=1
#high=n-1
def quick_sort(alist,start,end):
    #递归退出条件
    if start>=end:
        return
    #基准数
    mid=alist[start]
    low=start
    high=end

    while low<high:
        # 从右向左 alist[high]>mid 则high-=1
        while low < high and alist[high] >=mid:
            high -= 1
        # 将high索引对应的元素赋值给low
        alist[low] = alist[high]

        # 从左往右  alist[low]<mid  则low+=1
        while low < high and alist[low] < mid:
            low += 1

        alist[high] = alist[low]
    #将基准数放置到对应的位置
    alist[low]=mid

    #比基准数小的即左边的数据 要重复调用quick_sort()
    quick_sort(alist,start,low-1)
    #比基准数大的即右边的数据 要重复调用quick_sort()
    quick_sort(alist,low+1,end)

if __name__ == '__main__':
    alist=[54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('原数组：')
    print(alist)
    print('排序后数组：')
    quick_sort(alist,0,len(alist)-1)
    print(alist)