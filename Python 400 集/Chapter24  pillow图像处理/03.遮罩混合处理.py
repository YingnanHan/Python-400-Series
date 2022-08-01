'''
遮罩混合处理
在 Pillow 库中 Image 模块中，可以使用函数 composite()实现遮罩混合处理。具体语
法格式如下所示：
composite(im1,im2,mask)
其中 im1 和 im2 表示混合处理的图片 1 和图片 2.mask 也是一个图像，mode 可以为
“1”, “L”, or “RGBA”，并且大小要和 im1、im2 一样。
函数 composite()的功能是使用 mask 来混合图片 im1 和 im2，并且要求 mask、im1
和 im2 三幅图片的尺寸相同。下面的实例代码演示了使用 Image 模块实现图片遮罩
混合处理的过程
'''

from PIL import Image

img1 = Image.open("images/blend1.jpg")
img2 = Image.open("images/blend2.jpg")
img2.resize(img1.size)
r,g,b = img2.split()
Image.composite(img2,img1,b).show()