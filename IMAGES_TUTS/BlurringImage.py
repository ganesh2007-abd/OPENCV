import cv2 as cv

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")
cv.imshow("Original",img)

blurred = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blurred",blurred)

average = cv.blur(img,(3,3))
cv.imshow("Average",average)

median = cv.medianBlur(img,3)
cv.imshow("Median",median)

bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilateral",bilateral)
cv.waitKey(0)