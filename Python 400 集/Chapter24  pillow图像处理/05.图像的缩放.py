from PIL import Image
#按照像素缩放图片
img1 = Image.open("images/bjsxt.png")
#将每一个像素的大小扩大二倍
Image.eval(img1,lambda x:x*2).show()

