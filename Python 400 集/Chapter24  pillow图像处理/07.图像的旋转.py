'''
在 Pillow 库的 Image 模块中，函数 rotate()的功能返回此图像的副本，围绕其中心逆时
针旋转给定的度数。具体语法格式如下：
Image.rotate（angle，resample = 0，expand = 0，center = None，translate = None，fillcolor = None ）
'''
from PIL import Image
img = Image.open("images/bjsxt.png")
#将图片上下翻转180°
#img.rotate(180).show()

#将图片进行上下翻转
img.transpose(Image.FLIP_TOP_BOTTOM).show()
#将图片进行左右翻转
img.transpose(Image.FLIP_LEFT_RIGHT).show()
#将图片进行90°旋转
img.transpose(Image.ROTATE_90).show()
#将图片进行180°旋转
img.transpose(Image.ROTATE_180).show()
#将图片进行颠倒处理
img.transpose(Image.TRANSPOSE).show()