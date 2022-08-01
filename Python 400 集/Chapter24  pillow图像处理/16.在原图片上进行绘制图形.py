from PIL import ImageFont,ImageDraw,Image

img = Image.open("images/lena.jpg")
width,height = img.size
#创建绘图对象
drawObj = ImageDraw.Draw(img)
drawObj.arc((0,0,width-1,height-1),0,360,fill="blue")#在图片内部绘制一个圆形
#img.show()
