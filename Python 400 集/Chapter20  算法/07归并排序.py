[54, 26, 93, 17, 77, 31, 44, 55]  #升序排序
#分解  n//2
# [54, 26, 93, 17]   [77, 31, 44, 55]
#
# [54, 26]  [93, 17]   [77, 31]  [44, 55]
#
# [54]  [26]  [93] [17]   [77]  [31]  [44] [55]

#合并
# [26,54] [17,93] [31,77] [44,55]
#
# [17,26,(54,1),93]   [31,44,(54,2),55,77]
#
# [17,26,31,44,54,55,77,93]

def merg_sort(alist):
    #分解
    n=len(alist)
    #递归的出口 分解到最小
    if n<=1:
        return alist
    mid=n//2
    left_li=merg_sort(alist[0:mid])
    right_li=merg_sort(alist[mid:])

    #合并
    #排序结果列表
    result=[]
    left_pointer,right_pointer=0,0
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer] <=right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    #退出循环后，将不为空的列表剩余元素添加到result中
    # result+=left_li[left_pointer:]
    result.extend(left_li[left_pointer:])
    result+=right_li[right_pointer:]

    #将最后排序的结果列表返回
    return result



if __name__ =='__main__':
    alist=[54, 26, 93, 17, 77, 31, 44, 55]
    print('原来的数组：')
    print(alist)
    result=merg_sort(alist)
    print('排序后：')
    print(result)


