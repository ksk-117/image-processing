import cv2
import numpy as np
img = cv2.imread('pic/noise_mono.jpg')
cv2.imshow('img', img)
element8 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8)
dst1 = cv2.dilate(img, element8, iterations=1)
dst2 = cv2.erode(img, element8, iterations=1)
cv2.imshow('dilate', dst1)
cv2.imshow('erode', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
