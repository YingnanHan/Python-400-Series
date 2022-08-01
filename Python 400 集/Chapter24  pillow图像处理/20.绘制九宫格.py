from PIL import Image,ImageDraw

width,height = 300,300
img = Image.new("RGB",(width,height),(255,255,255))
draw_obj = ImageDraw.Draw(img)

def getColor(x,y):
    a = x//100 + y//100
    if a==0:
        return (255,0,0)
    elif a==1:
        return (255,255,0)
    elif a==2:
        return (255,255,255)
    elif a==3:
        return (0,0,255)
    elif a==4:
        return (0,255,255)
    else:
        return (0,0,0)

for x in range(width):
    for y in range(height):
        draw_obj.point((x,y),fill=getColor(x,y))

img.show()