import cv2 as cv

def face_detect_demo(img):
    #将图片灰度化
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # 加载人脸特征数据
    face_detect = cv.CascadeClassifier(
        'F:\\OpenCV\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
    # 对人脸进行检测  返回值是人脸的左上角矩形区域的坐标以及宽度和高度
    faces = face_detect.detectMultiScale(gray,scaleFactor=1.01,minNeighbors=3,maxSize=(33,33),minSize=(28,28))#后三个参数控制人脸检测的效果
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
        cv.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=2)
    #显示图片
    cv.imshow("img.jpg",img)


#加载图片
img = cv.imread("face2.jpg")
#调用人脸检测方法
face_detect_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()