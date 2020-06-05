import cv2

video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Cam", gray)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
