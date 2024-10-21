import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('pic/Parrots.bmp')
cv2.imshow("img", img)
height, width, channels = img.shape
mask = np.zeros((height, width, channels), np.uint8)
cv2.rectangle(mask, (0, 50), (85, height), (255, 255, 255), thickness=-1)
cv2.imshow("mask", mask)
dst = cv2.bitwise_and(img, mask)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
