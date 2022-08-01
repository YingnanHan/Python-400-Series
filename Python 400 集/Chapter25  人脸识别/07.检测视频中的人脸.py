import cv2 as cv

def face_detect_demo(frame):
    #将帧灰度处理
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #加载特征数据
    face_detector = cv.CascadeClassifier("F:\\OpenCV\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")
    #进行人脸检测
    faces = face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv.circle(frame, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=2)
    cv.imshow("result",frame)

#读取视频
cap = cv.VideoCapture("video.mp4")
#重复循环捕捉视频中的每一帧
while True:
    flag,frame = cap.read()
    print("flag:{0},frame:{1}".format(flag,frame))
    if not flag:    #如果视频播放完毕，则退出
        break
    face_detect_demo(frame)#frame参数是视频中的每一帧图像
    if ord('q') == cv.waitKey(10):#如果输入q则退出
        break
#释放空间
cv.destroyAllWindows()
cap.release()