import numpy as np

##创建随机小数构成的浮点数组
def randFloatTest():
    #使用random创建一维数组 [0.0,1.0)
    a = np.random.random(size=5)#生成五个0.0-1.0之间的随机数浮点数组
    print(a)
    print(type(a))

    #创建二维数组
    b = np.random.random(size=(3,4))#创建一个3x4的随机数浮点二维数组
    print(b)

    #创建三维数组
    c = np.random.random(size=(2,3,4))#创建一个2x3x4的随机数浮点三维数组
    print(c)

##创建随机整数的浮点数组
def randIntTest():
    #生成0-5之间的一尾随机整数数组
    a = np.random.randint(5,size=10)
    print(a)
    print(type(a))

    #生成5-10之间的随机正整数 二维
    b = np.random.randint(5,11,size=(4,3))#生成数据范围在5-10之间的4行3列的数组
    print(b)
    print(type(b))

    # 生成5-10之间的随机正整数 三维
    b = np.random.randint(5, 11, size=(4, 3,2))  # 生成数据范围在5-10之间的4个3行2列的数组
    print(b)
    print(type(b))

    #dtype的使用
    d = np.random.randint(10,size=5,dtype=np.int64)
    print("默认的dtype",d.dtype)#获得数组内元素的类型

##使用randn创建具有标准正态分布的数组
def randnTest():
    #生成一个具有4个元素的一维数组，数组中的元素服从标准正态分布均值为0方差为1
    a = np.random.randn(4)
    print(a)

    # 生成一个具有6个元素的二维数组，数组中的元素服从标准正态分布均值为0方差为1
    a = np.random.randn(2,3)
    print(a)

    # 生成一个具有8个元素的三维数组，数组中的元素服从标准正态分布均值为0方差为1
    a = np.random.randn(2, 2,2)
    print(a)

##创建具有指定期望与方差的正态分布
def normalTest():
    #在不指定期望与方差的情况下为标准正态分布
    a = np.random.normal(size=5)
    print(a)

    # 在指定期望与方差的情况下为标准正态分布  scale表示方差 loc表示期望
    a = np.random.normal(loc=2,scale=3,size=5)
    print(a)

normalTest()
