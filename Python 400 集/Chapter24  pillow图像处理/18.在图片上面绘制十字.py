from PIL import ImageFont,Image,ImageDraw

img = Image.open("images/blend1.jpg")
#img.show()
w,h = img.size
drawObj = ImageDraw.Draw(img)
drawObj.line((0,0,w,h),fill="blue",width=2)
drawObj.line((w,0,0,h),fill="red",width=2)
img.show()