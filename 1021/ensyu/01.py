import cv2
import numpy as np
def oresen(k):
    curve = k * np.arange(0, 256)
    curve = curve.clip(0, 255)
    return curve.astype(np.uint8)
img = cv2.imread('pic/Airplane.bmp')
curve = oresen(1.2)
dst = cv2.LUT(img, curve)
cv2.imshow('original', img)
cv2.imshow('dst 1.2', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
