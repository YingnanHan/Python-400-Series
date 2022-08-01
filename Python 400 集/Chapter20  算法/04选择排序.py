[7, 5, 3, 6, 44, 22, 99, 11]
[3, 5, 7, 6, 44, 22, 99, 11]  #第一次
[3, 5, 7, 6, 44, 22, 99, 11]  #第二次
[3, 5, 6, 7, 44, 22, 99, 11]  #第三次
[3, 5, 6, 7, 44, 22, 99, 11]  #第四次
[3, 5, 6, 7, 11, 22, 99, 44]  #第五次
[3, 5, 6, 7, 11, 22, 99, 44]  #第六次
[3, 5, 6, 7, 11, 22, 44, 99]  #第七次

[7, 5,(99,1), 3, 6, 44, 22, (99,2), 11]
[7, 5, 11,3, 6, 44, 22, (99,2),(99,1)]
#从列表中选择最大的元素放到最后一个位置
def select_sort(alist):
    n=len(alist)
    for i in range(n-1): # 0  n-1  O(n)
        #剩余列表中最小值的索引
        min_index=i
        for j in range(i+1,n): #O(n)
            if alist[min_index]>alist[j]:
                min_index=j
        if min_index!=i:
            alist[i],alist[min_index]=alist[min_index],alist[i]
alist=[7, 5, 3, 6, 44, 22, 99, 11]
print('原数组：')
print(alist)
print('排序后数组：')
select_sort(alist)
print(alist)