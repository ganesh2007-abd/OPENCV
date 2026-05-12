import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("IMAGES_TUTS\Sample_Imgs\Virat.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("Gray",gray)

ret1,simple_thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Simple Threshold",simple_thresh)

ret2,thresh_inv = cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)
cv.imshow("ThreshInverse",thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive Threshold",adaptive_thresh)
cv.waitKey(0)