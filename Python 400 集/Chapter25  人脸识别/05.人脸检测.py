import cv2 as cv

#人脸检测函数
def face_detect_demo():
    #将彩色图片进行灰度处理 减少色彩的通道 方便处理
    grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载人脸特征数据
    face_detect = cv.CascadeClassifier('F:\\OpenCV\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
    #对人脸进行检测  返回值是人脸的左上角矩形区域的坐标以及宽度和高度
    faces = face_detect.detectMultiScale(grey)
    for x,y,w,h in faces:
        #参数 图片对象 绘制图形的左上角坐标 右下角坐标 颜色设定
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
    cv.imshow("result",img)
#加载图片
img = cv.imread("lena.jpg")
#调用自定义人脸检测函数
face_detect_demo()
#显示图像
#cv.imshow("img",img)
#结束显示图像  使得图像持续在窗口中显示
cv.waitKey(0)
cv.destroyAllWindows()