import cv2 as cv
img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\StarryNight.jpg")
cv.imshow("Night image",img)
k=cv.waitKey(0)
if k == ord('s'):
    cv.imwrite("Night_Image_sample.png",img)