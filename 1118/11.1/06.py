import cv2
import numpy as np
bg = cv2.imread('pic/frame_0.jpg', cv2.IMREAD_GRAYSCALE)
flame = cv2.imread('pic/frame_1.jpg', cv2.IMREAD_GRAYSCALE)
diff = cv2.absdiff(flame, bg)
cv2.imshow('diff', diff)
mask = cv2.threshold(diff, 40, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((3, 3), np.uint8)

