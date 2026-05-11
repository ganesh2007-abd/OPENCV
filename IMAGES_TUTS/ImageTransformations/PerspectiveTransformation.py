import cv2 as cv
import numpy as np

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
width = img.shape[1]
height = img.shape[0]
pts1 = np.float32([[20,30],[40,50],[10,6],[50,60]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

M=cv.getPerspectiveTransform(pts1,pts2)
perpectedimage = cv.warpPerspective(img,M,(width,height))
cv.imshow("Normal",img)
cv.imshow("Perspected",perpectedimage)
cv.waitKey(0)