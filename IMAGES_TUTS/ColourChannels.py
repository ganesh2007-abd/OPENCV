import cv2 as cv
import numpy as np


img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Virat",img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)

cv.imshow("Blue GrayScale",b)
cv.imshow("Green GrayScale",g)
cv.imshow("Red GrayScale",r)

#Merging Brooo

original = cv.merge([b,g,r])

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

org = cv.merge([blue,green,red])

cv.waitKey(0)