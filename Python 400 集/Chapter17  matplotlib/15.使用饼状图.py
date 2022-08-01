#导入模块
import matplotlib.pyplot as plt
import numpy as np
#准备男，女的人数以及比例
man = 71351
woman  =  68187
man_perc = man/(woman+man)

#解决乱码问题
plt.rcParams["font.sans-serif"]=["SimHei"]

#添加颜色
color = ["blue","red"]

#添加名称标签
labels = ["m","w"]
woman_perc = woman / (woman+man)
#                     explode表示把每一个分块分隔开 autopct设置比例显示格式 %<目标格式>%
plt.pie([man,woman],labels=labels,colors=color,explode=(0.0,0.05),autopct="%0.1f%%")

plt.show()