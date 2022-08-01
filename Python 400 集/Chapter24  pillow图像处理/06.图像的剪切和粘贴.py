from PIL import Image

img = Image.open("images/bjsxt.png")
#赋复制操作
imgb = img.copy()
imgc = img.copy()
#剪切操作
img_proc = imgb.crop((10,10,120,120))#这里所说的剪切指的是将原来的图片的某一部分剪切下来，这一部分有坐标元组指定
#粘贴
imgc.paste(img_proc,(30,30))#将裁剪下来的图片部分粘贴到imgc上
imgc.show()