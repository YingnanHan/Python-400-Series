'''
内置的 ImageEnhance 模块中包含了多个用于增强图像效果的函数，主要用来调整图像
的色彩、对比度、亮度和清晰度等，感觉上和调整电视机的显示参数一样。
在模块 ImageEnhance 中，所有的图片增强对象都实现一个通用的接口。这个接口只包
含如下一个方法。
方法 enhance()会返回一个增强的 Image 对象，参数 factor 是一个大于 0 的浮点数，1 表
示返回原始图片。
当在 Python 程序中使用模块 ImageEnhance 增强图像效果时，需要首先创建对应的增强
调整器，然后调用调整器输出函数，根据指定的增强系数（小于 1 表示减弱，大于 1 表示增
强，等于 1 表示原图不变）进行调整，最后输出调整后的图像。
在模块 ImageEnhance 中，常用的内置函数如下所示：
（1）ImageEnhance.Color（image ）：功能是调整图像色彩平衡，相当于彩色电视机的
色彩调整，实现了上边提到的接口的 enhance 方法。
（2）ImageEnhance.Contrast（image ）：功能是调整图像对比度，相当于彩色电视机的
对比度调整。
（3）ImageEnhance.Brightness（image ）：功能是调整图像亮度。
（4）ImageEnhance.Sharpness（image ）：功能是调整图像清晰度，用于锐化/钝化图片。
锐化操作的 factor 是 0~2 之间的一个浮点数。当 factor=0 时，返回一个模糊的图片对
象；当 factor=2 时，返回一个锐化的图片对象；当 factor=1 时，返回原始图片对象
'''
from PIL import Image,ImageChops,ImageFilter,ImageEnhance
#打开图像
img = Image.open("images/blend1.jpg")
#img.show()
w,h = img.size
img_output = Image.new("RGB",(3*w,h))
img_output.paste(img,(0,0))

#色彩增强效果示例
#获取色彩调整器
img_color = ImageEnhance.Color(img)
img1 = img_color.enhance(1.5)#为图像效果进行增强色彩效果
img_output.paste(img1,(w,0))

#色彩减弱效果示例
#获取色彩调整器
img2 = img_color.enhance(0.5)#为图像效果进行增强色彩效果
img_output.paste(img2,(2*w,0))

img_output.show()