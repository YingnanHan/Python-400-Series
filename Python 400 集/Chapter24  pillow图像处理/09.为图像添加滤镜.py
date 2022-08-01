from PIL import Image,ImageFilter
#01
# img = Image.open("images/bjsxt.png")
# img = img.filter(ImageFilter.GaussianBlur)#使用GaussBlur滤镜对图像进行模糊操作
# img.show()

#02
# img = Image.open("images/lena.jpg")
# img = img.filter(ImageFilter.GaussianBlur)#使用GaussBlur滤镜对图像进行模糊操作
# img.show()

#03 制作原图像与模糊图像的对比图
img = Image.open("images/lena.jpg")
w,h = img.size
#创建一个图像
img_out = Image.new("RGB",(2*w,h))
img_out.paste(img,(0,0))

img_filter = img.filter(ImageFilter.GaussianBlur)#为图像添加滤镜
img_out.paste(img_filter,(w,0))
img_out.show()