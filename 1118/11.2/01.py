import cv2
cap = cv2.VideoCapture(0)
cascade = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        face = cascade.detectMultiScale(frame)
        if len(face) > 0:
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('映像未取得')
        break
cap.release()
cv2.destroyAllWindows()
