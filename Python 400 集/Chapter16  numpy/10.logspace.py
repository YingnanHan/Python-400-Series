'''
numpy.logspace函数用于创建一个于等比数列。
格式如下：np.logspace(start,stop,num=50,endpoint=True,base=10.0,dtype=None)
logspace参数说明参数描述
start序列的起始值为：base**start
stop序列的终止值为：base**stop。
如果endpoint为true，该值包含于数列中num要生成的等步长的样本数量，默认为50
endpoint该值为ture时，数列中中包含stop值，反之不包含，默认是True。
base对数log的底数。
dtypendarray的数据类型
'''

import numpy as np

def logspaceTest():

    n  = np.logspace(1,10,5,base=5,dtype=int)
    print(n)

logspaceTest()
