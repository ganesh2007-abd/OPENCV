import cv2 as cv
import numpy as np
img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\StarryNight.jpg")
(height,width) = img.shape[:2]
M = np.float32([[1,0,10],[0,1,20]])
transformed = cv.warpAffine(img,M,(width,height))
cv.imshow("Normal",img)
cv.imshow("Trnasformed",transformed)

cv.waitKey(0)