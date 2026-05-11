import cv2 as cv
import numpy as np

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Kohli",img)

canny = cv.Canny(img,125,175)

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found(Without Blur)')

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)

cv.drawContours(blank,contours,-1,(0,255,0),thickness=1)
cv.imshow("With contours",blank)

blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
blank2 = np.zeros(img.shape,dtype='uint8')

canny2 = cv.Canny(blur,125,175)

contours2,hierarchies = cv.findContours(canny2,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours2)} contours found(With Blur)')

cv.drawContours(blank2,contours2,-1,(0,255,0),thickness=1)
cv.imshow("With contours Blur",blank2)

cv.waitKey(0)

