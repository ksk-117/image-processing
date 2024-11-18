import cv2
import numpy as np
img = cv2.imread('pic/flower04.jpg')
cv2.imshow('img', img)
lower = np.array([130, 50, 50])
upper = np.array([160, 255, 255])
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
result = cv2.inRange(hsv, lower, upper)
kernel = np.ones((5, 5), np.uint8)
result = cv2.morphologyEx(result, cv2.MORPH_OPEN, kernel)
contours, hiera = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(img)
dst = cv2.bitwise_and(img, mask)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
cv2.imshow('dst_with_rect', img)
cv2.waitKey(0)
cv2.destroyAllWindows()