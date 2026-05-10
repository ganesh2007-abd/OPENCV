import cv2 as cv

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
blurred = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Original",img)
cv.imshow("Blurred",blurred)

cv.waitKey(0)