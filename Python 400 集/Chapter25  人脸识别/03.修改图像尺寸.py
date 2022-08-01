import cv2 as cv

img = cv.imread("lena.jpg")
#修改的图像保存至newImage里面
newImage = cv.resize(img,dsize=(200,200))
#显示新修改的图像
cv.imshow("resized Image",newImage)
#使用shape属性查看图像的长宽等属性
print(img.shape)#高×宽×颜色通道
print(newImage.shape)#高×宽×颜色通道

#设置输入q键退出图片显示
while True:
    if  cv.waitKey(0)==ord('q'):
        break

cv.destroyAllWindows()