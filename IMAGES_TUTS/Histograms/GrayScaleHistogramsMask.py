import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("IMAGES_TUTS\Sample_Imgs\Virat.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Kohli",img)

blank = np.zeros(img.shape[:2],dtype='uint8')

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),80,255,-1)

# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow("Mkased",masked)


cv.imshow("Grayed",gray)
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title("Mask Grayscale")
plt.xlabel("Intensity")
plt.ylabel("No of pixels")
plt.plot(gray_hist)
plt.xlim([0,255])
plt.show()