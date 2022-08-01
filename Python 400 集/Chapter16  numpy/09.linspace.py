'''
linspace函数用于创建一个一维数组，数组是一个等差数列构成的，
格式如下：np.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
linspace参数说明参数描述start序列的起始值stop序列的终止值，如果endpoint为true，
该值包含于数列中num要生成的等步长的样本数量，默认为50
endpoint该值为ture时，数列中中包含stop值，反之不包含，默认是True。
retstep如果为True时，生成的数组中会显示间距，反之不显示。
dtypendarray的数据类型'''

import numpy as np

def linspaceTest():

    n  = np.linspace(5,10,4,dtype=int)
    print(n)

    n = np.linspace(5, 10, 4,endpoint=False,dtype=int)
    print(n)

linspaceTest()
