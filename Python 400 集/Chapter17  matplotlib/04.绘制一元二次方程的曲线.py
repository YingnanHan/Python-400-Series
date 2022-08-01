import matplotlib.pyplot as plt

#生成200点的坐标
x = [i for i in range(-200,200)]
y = [i**2 for i in range(-200,200)]

#绘制一元二次方程的曲线
plt.plot(x,y)

#保存图片到本地
#plt.savefig("Square")#默认生成图片的格式是png
plt.savefig("Sqare.jpg")
plt.show()