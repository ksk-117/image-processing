import cv2
from matplotlib import pyplot as plt
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow("img", img)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 255])
    plt.plot(hist, color=col)
plt.show()
