import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('pic/Mandrill.bmp', 0)
cv2.imshow("img1", img1)
img2 = cv2.imread('pic/Parrots.bmp', 0)
cv2.imshow("img2", img2)
hist_img1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
hist_img2 = cv2.calcHist([img2], [0], None, [256], [0, 255])
plt.plot(hist_img1, label='img1')
plt.plot(hist_img2, label='img2')
plt.legend()
plt.show()
