import cv2 as cv
import numpy as np

img = cv.imread("IMAGES_TUTS\Sample_Imgs\RCB_SQUAD3.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayed",gray)

face_detector = cv.CascadeClassifier("IMAGES_TUTS\FaceDetection\haar_face_def.xml")
face_cord = face_detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

for (x,y,w,h) in face_cord:
    cv.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow("Faces",gray)



cv.waitKey(0)