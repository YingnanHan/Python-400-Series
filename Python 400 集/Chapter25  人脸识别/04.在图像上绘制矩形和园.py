import cv2 as cv

img = cv.imread("lena.jpg")
#定义左上角的坐标
x,y,w,h = 100,100,100,100
#绘制矩形
rect = cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,0),thickness=2)#BGR
cv.imshow("rectangle.jpg",rect)

#绘制圆形
x,y,r = 200,200,100
circle = cv.circle(img,center=(x,y),radius=r,color=(0,0,255),thickness=2)
cv.imshow("circle.jpg",circle)

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()