import cv2
import numpy as np
from matplotlib import pyplot as plt
img =np.title(np.arange(0, 256, 1, dtype=np.uint8),(256, 1)).reshape(256, 256)
ret,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

