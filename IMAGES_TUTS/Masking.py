import cv2 as cv
import numpy as np

img = cv.imread("IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Kohli",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),80,255,-1)
cv.imshow("Mask",blank)

masked = cv.bitwise_and(img,img,mask=blank)
cv.imshow("Masked",masked)

cv.waitKey(0)