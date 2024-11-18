import cv2
import numpy as np
cap = cv2.VideoCapture(0)
ret, bg = cap.read()
bg_gray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(frame_gray, bg_gray)
    th = cv2.threshold(diff, 60, 255, cv2.THRESH_BINARY)[1]
    element4 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, element4)
    contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            frame = cv2.putText(frame, 'detected', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    cv2.imshow('Difference', th)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
