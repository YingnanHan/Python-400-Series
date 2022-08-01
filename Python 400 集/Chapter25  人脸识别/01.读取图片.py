#导入模块
import cv2 as cv
#读取图片
img = cv.imread("lena.jpg")#注意在读取图片的时候路径不能有中文字符
#显示图片
cv.imshow("read_img",img)#第一个参数是图像的自定义名称，第二个参数是图像对象
cv.waitKey(1000)#等待键盘输入参数，等待x毫秒之后关闭图像  如果参数==0那么不会关闭图像
#释放图像对象所占用内存(opencv底层是C++没有自动垃圾回收机制)
cv.destroyAllWindows()