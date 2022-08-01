import numpy as np
#注意所有的操作都是建立在转化为np.array类型的基础上的
A = np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])
#垂直分割为2分
r,w = np.vsplit(A,2)
print(r)
print(w)
print("-----------")
#按位置分割为k分
o,p,q = np.vsplit(A,[3,4])
print(o,"\n",p,"\n",q)