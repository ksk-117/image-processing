import cv2
import numpy as np
img = cv2.imread('pic/crescent.png', 0)
cv2.imshow('img', img)
contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contours[0])
perimater = cv2.arcLength(np.array(contours[0]), True)
roundness = 4 * np.pi * area / (perimater * perimater)
print('area=', area)
print('perimeter=', perimater)
print('roundness=', roundness)
cv2.waitKey(0)
cv2.destroyAllWindows()
