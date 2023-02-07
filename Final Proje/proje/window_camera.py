import cv2


def camera():#this is the function of using camera

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)
        c = cv2.waitKey(1)
        if c == 27:  #(27= Ecs key) When we press esc, the camera turns off
            break
    cap.release()
    cv2.destroyAllWindows()
