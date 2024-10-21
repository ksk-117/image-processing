import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == False:
        print('カメラから映像を取得できませんでした')
        break
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('cap.jpg', frame)
        break
cap.release()
cv2.destroyAllWindows()
