import cv2 as cv

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
(height,width) = img.shape[:2]
scaled_withoutfactors = cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)
cv.imshow("normal",img)
cv.imshow("Scaled",scaled_withoutfactors)

scaled_withfactors = cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
cv.imshow("Sclaed(fx,fy)",scaled_withfactors)
cv.waitKey(0)