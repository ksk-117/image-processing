import cv2
import numpy as np
I1 = cv2.imread('pic/frame_0.jpg', cv2.IMREAD_GRAYSCALE)
I2 = cv2.imread('pic/frame_1.jpg', cv2.IMREAD_GRAYSCALE)
I3 = cv2.imread('pic/frame_2.jpg', cv2.IMREAD_GRAYSCALE)
img_diff1 = cv2.absdiff(I1, I2)
img_diff2 = cv2.absdiff(I2, I3)
cv2.imshow('img_diff1', img_diff1)
cv2.imshow('img_diff2', img_diff2)
img_and = cv2.bitwise_and(img_diff1, img_diff2)
img_th = cv2.threshold(img_and, 40, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((3, 3), np.uint8)
img_dilate = cv2.dilate(img_th, kernel, iterations=2)
img_mask = cv2.erode(img_dilate, kernel, iterations=2)
cv2.imshow('mask', img_mask)
dst = cv2.bitwise_and(I2, img_mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
