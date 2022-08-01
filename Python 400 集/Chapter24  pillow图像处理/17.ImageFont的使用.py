from PIL import Image,ImageFont,ImageDraw

img = Image.open("images/bjsxt.png")
print(img.size)
draw_obj = ImageDraw.Draw(img)
#font = ImageFont.load_default()#加载系统默认的字体与默认大小
font = ImageFont.truetype("simhei.ttf",18)#使用自定义的字体与默认大小
draw_obj.text((30,10),text="Peking SXT",fill="white",font=font)
img.show()