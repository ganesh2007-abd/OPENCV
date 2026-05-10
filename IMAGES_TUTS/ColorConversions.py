import cv2 as cv
img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("BGR",img)
cv.imshow("GRAY",gray)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

cv.waitKey(0)