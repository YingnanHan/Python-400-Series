from PIL import Image

img1 = Image.open("images/bjsxt.png").convert(mode='RGB')
img2 = Image.new('RGB',img1.size,'red')

#img2.show()
Image.blend(img1,img2,alpha=0.5).show()