from PIL import Image
#打开图片
img = Image.open("images\\bjsxt.png")
#显示图片
img.show()
#获取图片信息
print("图片格式:",img.format)
print("图片大小:",img.size)
print("图片高度:",img.height,"图片宽度:",img.width)
print("获取一点处的像素值",img.getpixel((100,100)))#返回值以RGB形式给出
