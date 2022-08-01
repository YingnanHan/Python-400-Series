#使用循环实现二分法（非递归）
def binary_search(alist,v):
    n=len(alist)
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        #判断中间值与比较的值v
        if alist[mid] == v:
            return True
        elif alist[mid] > v: #左边列表查找
            end=mid-1
        else:
            start=mid+1
    return False

#递归方式实现
def binary_search2(alist,v):
    n=len(alist)
    #递归出口
    if n==0:
        return False
    mid=n//2
    if alist[mid] == v:
        return True
    elif alist[mid] < v: #右边列表查找
        return binary_search(alist[mid+1:],v)
    else :
        return  binary_search(alist[0:mid],v)

if __name__ == '__main__':
    alist=[1,2,3,4,5,6,7,8,9]
    print(binary_search(alist,9))
    print(binary_search(alist,19))
    print(binary_search2(alist,9))
    print(binary_search2(alist,19))
