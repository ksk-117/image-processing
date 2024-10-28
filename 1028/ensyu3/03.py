import cv2
import numpy as np
img = cv2.imread('pic/labeling.png', 0)
num_lab, img_lab = cv2.connectedComponents(img)
print('num_lab =', num_lab)
labels_to_compare = [5, 15, 25, 35, 45]
masks = [cv2.compare(img_lab, np.full(img_lab.shape, label, dtype=np.int32), cv2.CMP_EQ) for label in labels_to_compare]
dst = np.zeros_like(img_lab, dtype=np.uint8)
for mask in masks:
    dst = cv2.bitwise_or(dst, mask)
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()