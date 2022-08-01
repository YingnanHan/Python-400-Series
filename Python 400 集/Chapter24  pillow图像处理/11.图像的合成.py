'''
The ImageChops module contains a number of arithmetical image operations,
called channel operations (“chops”). These can be used for various purposes,
including special effects, image compositions, algorithmic painting, and more.
'''
from PIL import Image,ImageChops
#打开图片
img1 = Image.open("images/blend1.jpg")
img2 = Image.open("images/blend2.jpg")
#对图像进行 add()运算
ImageChops.add(img1,img2).show()
#对图像进行 subtract()运算
ImageChops.subtract(img1,img2).show()
#对图像进行 darker()运算
ImageChops.darker(img1,img2).show()
#对图像进行 lighter()运算
ImageChops.lighter(img1,img2).show()
#对图像进行 multiply()运算
ImageChops.multiply(img1,img2).show()#效果叠加
#对图像进行 screen()运算
ImageChops.screen(img1,img2).show()
#对图像进行 invert()运算 只接收一个参数 255-每一个点的像素值
ImageChops.invert(img1).show()
#比较函数 difference()  将两个图片的像素值相减得到绝对值
ImageChops.difference(img1,img2).show()