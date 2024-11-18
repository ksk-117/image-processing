import cv2
cap = cv2.VideoCapture('pic/vtest.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
for n in range(3):
    cap.set(cv2.CAP_PROP_POS_FRAMES, round(n*fps))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('{}_{}.{}'.format('pic/frame', str(n), 'jpg'), frame)
    else:
        print('映像未取得')
        break
cap.release()
cv2.destroyAllWindows()
