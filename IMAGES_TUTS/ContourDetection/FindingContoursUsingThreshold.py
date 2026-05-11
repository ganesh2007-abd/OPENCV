import cv2 as cv
import numpy as np

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Kohli",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresholded image",thresh)

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found(Without Blur)')

cv.drawContours(blank,contours,-1,(0,255,0),thickness=1)
cv.imshow("With contours",blank)

cv.waitKey(0)