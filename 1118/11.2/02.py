import cv2
from ultralytics import YOLO
medel = YOLO('yolov8n.pt')
cap = cv2.VideoCapture('pic/vtest.avi')
while True:
    ret, frame = cap.read()
    if ret:
        results = medel.track(frame, persist=True)
        frame_track = results[0].pllot()
        cv2.imshow('Tracking', frame_track)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('映像未取得')
        break
cap.release()
cv2.destroyAllWindows()
