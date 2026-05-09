import cv2 as cv

def rescale(frame,scalevalue=0.75):
    width = int(frame.shape[1] * scalevalue)
    height = int(frame.shape[0] * scalevalue)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if not ret:
        print("Video Ended")
        break
    resized_frame = rescale(frame)
    cv.imshow("Normal Video",frame)
    cv.imshow("Resized Video",resized_frame)

    if cv.waitKey(1) == ord('q'):
        print("You interrupted")
        break
cap.release()
cv.destroyAllWindows()