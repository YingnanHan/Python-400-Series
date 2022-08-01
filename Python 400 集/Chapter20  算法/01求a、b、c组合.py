#如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time
start_time=time.time()
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a+b+c==1000 and a**2+b**2==c**2:
                print('a:',a,'b:',b,'c:',c)
#f(n)=n*n*n*2
#获取时间
end_time=time.time()
print('所花费时间：',(end_time-start_time))

#T(n)=k*f(n)+c
#f(n)=n*n
#f(n)叫做T(n)的渐进函数
# T(n)=O(f(n))

#对列表进行排序
#[9,8,7,6,5,4,3,2,1] 进行升序排序

# [1,2,3,4,5,6,7,8,9] 进行升序排序
print('a')
print('b')