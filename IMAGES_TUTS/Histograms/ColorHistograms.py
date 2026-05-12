import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Original",img)

colors = ('b','g','r')


plt.figure()
plt.title("Colours Histogram")
plt.xlabel("Intesity")
plt.ylabel("No of pixels")

for i,col in enumerate(colors):
    col_hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(col_hist,color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)