import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Original",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),80,255,2)

colors = ('b','g','r')

plt.figure()
plt.title("Maksed Colour Histograms")
plt.xlabel("INtensity")
plt.ylabel("No of pixels")

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)