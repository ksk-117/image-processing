import numpy as np
import cv2
height = 100
width = 200
cannel = 3
value1 = (0, 0, 255)
value2 = (0, 255, 0)
img1 = np.full((height, width, cannel), value1, np.uint8)
img2 = np.full((height, width, cannel), value2, np.uint8)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
