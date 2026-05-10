import cv2 as cv

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\Virat.jpg")

edged = cv.Canny(img,125,175)
cv.imshow("Edge",edged)

dilated = cv.dilate(edged,(7,7),iterations=3)
cv.imshow("Dilated",dilated)

eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)

cv.waitKey(0)