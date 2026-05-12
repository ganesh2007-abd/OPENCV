import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Original",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grayScale",gray)

gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("Gray Scale Histograms")
plt.xlabel("Intensity of pixel")
plt.ylabel("No of pixels")
plt.plot(gray_hist)
plt.xlim([0,255])
plt.show()

cv.waitKey(0)