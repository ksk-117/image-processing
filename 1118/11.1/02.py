import cv2
cap = cv2.VideoCapture('pic/vtest.avi')
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('映像未取得')
        break
cap.release()
cv2.destroyAllWindows()
