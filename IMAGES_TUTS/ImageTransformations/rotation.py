import cv2 as cv

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
height,width = img.shape[:2]
M = cv.getRotationMatrix2D((width/2.0,height/2.0),90,1)

rotated = cv.warpAffine(img,M,(width,height))
cv.imshow("Rotated",rotated)
cv.waitKey(0)