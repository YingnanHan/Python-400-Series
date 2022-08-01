from PIL import Image
img = Image.open("images/blend1.jpg")
w,h = img.size  #size是一个属性
img_output = Image.new("RGB",(3*w,h))
img_output.paste(img,(0,0))
#使用point()函数对当前图像的整体像素点进行像素的运算，用来控制亮度
#图像整体变量
imgb = img.point(lambda i:i*1.5)#使得所有的像素点的像素值变大为原来的1.5倍
#图像整体变暗
imgc = img.point(lambda i:i*0.4)

img_output.paste(imgb,(w,0))
img_output.paste(imgc,(2*w,0))

img_output.show()