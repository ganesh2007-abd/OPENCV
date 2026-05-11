import cv2 as cv
import numpy as np
img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\StarryNight.jpg")
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
transformed = cv.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv.imshow("Transformed",transformed)
cv.waitKey(0)