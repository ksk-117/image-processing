import cv2
cap = cv2.VideoCapture('pic/vtest.avi')
while True:
    ret, frame = cap.read()
    if ret:
        dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('dst', dst)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('映像未取得')
        break
cap.release()
cv2.destroyAllWindows()
