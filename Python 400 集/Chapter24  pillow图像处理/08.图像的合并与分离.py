from PIL import Image

img1 = Image.open("images/blend1.jpg")
img2 = Image.open("images/blend2.jpg")
img2 = img2.resize(img1.size)
#分割
r1,g1,b1 = img1.split()
r2,g2,b2 = img2.split()
temp = [r1,b2,b1]
#合并
img = Image.merge('RGB',temp)
img.show()