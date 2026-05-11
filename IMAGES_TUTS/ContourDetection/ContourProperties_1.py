import cv2 as cv
import numpy as np

# blank = np.zeros((700,700),dtype='uint8')

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Flash.png")
img = cv.resize(img,(700,700),interpolation=cv.INTER_AREA)
cv.imshow("Original",img)
original = img.copy()
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,img = cv.threshold(img,1,255,cv.THRESH_BINARY)

# cv.rectangle(blank,(300,300),(500,600),255,-1)
# cv.imshow("Rectangle",blank)

contours,hier = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

cnt = max(contours, key=cv.contourArea)
# print(contours[3])

area = cv.contourArea(cnt)
print(f"{area} is the area of contour")

per = cv.arcLength(cnt,True)
print(f"{per} is perimeter of the contour")

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(original,(x,y),(x+w,y+h),(0,255,0),8)
cv.imshow("BoundedRectangle",original)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = box.astype(int)
cv.drawContours(original,[box],-1,(0,0,255),2)
cv.imshow("Min rectangle",original)

(x,y),r = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(r)
cv.circle(original,center,radius,(255,0,0),2)
cv.imshow("Circle",original)

elli = cv.fitEllipse(cnt)
cv.ellipse(original,elli,(20,255,255),2)
cv.imshow("Ellipse",original)

cv.waitKey(0)

