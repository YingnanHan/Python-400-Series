#调用cv.cvt函数执行此任务
import cv2 as cv

#加载图像
img = cv.imread("lena.jpg")
#显示图像
#cv.imshow("BGR_img",img)

#将图像进行灰度转换
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#调用函数显示新图像
cv.imshow("Grey Image",gray_img)
#将生成的图片进行保存
cv.imwrite("gey_lena.jpg",gray_img)#第一个参数是保存文件名，第二个是图像对象

#等待按下按键并销毁内存
cv.waitKey(0)
cv.destroyAllWindows()