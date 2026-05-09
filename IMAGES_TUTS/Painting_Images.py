import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

# cv.imshow("Blank Image",blank)
# cv.waitKey(0)
# cv.destroyAllWindows()

cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
# cv.imshow("line Image",blank)
# cv.waitKey(0)
# cv.destroyAllWindows()

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=5)
# cv.imshow("Hollow Rectangle Image",blank)
# cv.waitKey(0)
# cv.destroyAllWindows()

cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=cv.FILLED)
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
# cv.imshow("Filled Rectangle Image",blank)
# cv.waitKey(0)
# cv.destroyAllWindows()

cv.circle(blank,(250,250),50,(255,0,0),thickness=cv.FILLED)
# cv.imshow("Filled Rectangle Image",blank)
# cv.waitKey(0)
# cv.destroyAllWindows()

cv.putText(blank,"Ganesh",(300,250),cv.FONT_HERSHEY_COMPLEX,1.0,(60,48,60),thickness=4)
cv.imshow("Filled Rectangle Image",blank)
cv.waitKey(0)
cv.destroyAllWindows()