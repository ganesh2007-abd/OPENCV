import cv2 as cv
cap = cv.VideoCapture("D:\SKILLS\OPENCV\VIDEOS_TUTS\SAMPLE_VIDEOS\SAMPLE_VIDEO_1.mp4")

while True:
    ret,frame = cap.read()

    if not ret:
        print("Video Completed")
        break

    cv.imshow("Video Window",frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()