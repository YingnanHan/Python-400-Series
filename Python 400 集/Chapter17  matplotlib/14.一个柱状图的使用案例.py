#导入模块
import matplotlib.pyplot as plt
import numpy as np
#准备数据
#三部电影的名称
real_names=['千与千寻','玩具总动员4','黑衣人：全球追缉']
#3天内票房书
real_num1=[7548,4013,1673]
real_num2=[5453,1840,1080]
real_num3=[4348,2345,1890]
x=np.arange(len(real_names))
#绘制柱状图
width=0.3
plt.bar(x,real_num1,alpha=0.5,width=width,label=real_names[0])
plt.bar([i+width for i in x],real_num2,alpha=0.5,width=width,label=real_names[1])
plt.bar([i+2*width for i in x],real_num3,alpha=0.5,width=width,label=real_names[2])
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#设置x坐标的值  第1天   第2天   第3天
x_label=['第{}天'.format(i+1) for i in x]
# print(x_label)
plt.xticks([i+width for i in x],x_label)
#添加ylabel
plt.ylabel('票房数')
#添加图例
plt.legend()
#添加标题
plt.title('3天3部电影票房数')
plt.show()