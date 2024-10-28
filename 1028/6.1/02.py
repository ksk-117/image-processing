import cv2
import numpy as np
img = cv2.imread('noise_mono.jpg')
cv2.imshow('img', img)
element4 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
dst1 = cv2.morpfologyEx(img, cv2.MORPH_OPEN, element4, iterations=1)
dst2 = cv2.morpfologyEx(img, cv2.MORPH_CLOSE, element4, iterations=1)
dst3 = cv2.morphologyEx(dst1, cv2.MORPH_CLOSE, element4, iterations=1)
cv2.imshow('open', dst1)
cv2.imshow('close', dst2)
cv2.imshow('open+close', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
