from PIL import ImageDraw,Image,ImageFont,ImageEnhance
import random

width,height = 100,100

img = Image.new("RGB",(width,height),(255,255,255))

draw_obj = ImageDraw.Draw(img)

#生成随机颜色
def getColor():
    return (random.randint(200,255),random.randint(200,255),random.randint(200,255))

for x in range(100):
    for y in range(100):
        draw_obj.point((x,y),fill=getColor())

#生成随机字母
def getchar():
    return chr(random.randint(65,97))

font = ImageFont.truetype("simhei.ttf",36)

#绘制随机字母
for i in range(4):
    draw_obj.text((10+i*20,40),getchar(),fill=(255,0,0),font=font)

#绘制干扰线
draw_obj.line((0,0,100,100),fill=(255,125,111))

img.show()