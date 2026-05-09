import cv2 as cv
def rescale(frame,scalevalue=0.75):
    width = int(frame.shape[1] * scalevalue)
    height = int(frame.shape[0] * scalevalue)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread("D:\SKILLS\OPENCV\IMAGES_TUTS\Sample_Imgs\StarryNight.jpg")
img_resized = rescale(img)

cv.imshow("Normal",img)
cv.imshow("Resized",img_resized)

cv.waitKey(0)
cv.destroyAllWindows()