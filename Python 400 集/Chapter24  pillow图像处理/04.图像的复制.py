from PIL import Image
img1 = Image.open("images/bjsxt.png")
#按尺寸进行缩放图片
#复制图片
img2 = img1.copy()
img1.show()
#进行缩放  对img2本身进行修改
img2.thumbnail((200,160)).show()