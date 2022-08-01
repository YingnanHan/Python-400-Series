from PIL import ImageDraw,Image

img = Image.open("images/bjsxt.png")
draw_obj = ImageDraw.Draw(img)
width,height = img.size

def getcolor(oldColor):
    #将黄色像素修改为红色像素
    #获取每一个通道的像素值 黄色 (255,255,0)
    if oldColor[0]>60 and oldColor[1]>60:#如果通道满足这两个条件，那么对外显示的就是偏黄的颜色
        return (oldColor[0],0,oldColor[2])#将绿色通道设置为0，那么对外显示的就是偏红的颜色
    else:
        return oldColor

for x in range(width):
    for y in range(height):
        #获得当前坐标处的色彩
        oldColor = img.getpixel((x,y))
        draw_obj.point((x,y),fill=getcolor(oldColor))

img.show()
