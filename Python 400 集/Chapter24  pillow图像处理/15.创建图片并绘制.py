from PIL import Image,ImageDraw,ImageFont

#新建一张白底图片
img = Image.new("RGB",(300,300),'white')
#img.show()

#得到画笔对象
drawObj = ImageDraw.Draw(img)
#在对应图片上绘制图形
drawObj.rectangle((50,50,250,250),outline="red",fill="blue")
#在对应图片上绘制文本
font = ImageFont.truetype("ARIALNBI.TTF",20)#创建字体对象
drawObj.text((100,100),"Hello",font=font,fill="white")#在绘制之前需要设置好字体
#显示最终的图形
img.show()
