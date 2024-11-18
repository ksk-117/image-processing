import cv2
import numpy as np
bg = cv2.imread('pic/frame_0.jpg', cv2.IMREAD_GRAYSCALE)
frame = cv2.imread('pic/frame_1.jpg', cv2.IMREAD_GRAYSCALE)
diff = cv2.absdiff(frame, bg)
cv2.imshow('diff', diff)
mask = cv2.threshold(diff, 40, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((3, 3), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=2)
mask = cv2.erode(mask, kernel, iterations=2)
cv2.imshow('mask', mask)
dst = cv2.bitwise_and(frame, mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
