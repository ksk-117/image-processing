import cv2
import matplotlib.pyplot as plt
import numpy as np
def gamma_curve(gamma):
    curve = np.arange(0, 256)
    curve = 255 * np.power(curve / 255, 1/gamma)
    return curve.astype(np.uint8)
src = cv2.imread('pic/Mandrill.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)
curve1 = gamma_curve(0.5)
dst = cv2.LUT(src, curve1)
cv2.imshow('dst 0.5', dst)
curve2 = gamma_curve(2)
dst = cv2.LUT(src, curve2)
cv2.imshow('dst 2', dst)
plt.subplot(121)
plt.plot(curve1), plt.title('k=0.5')
plt.xlim(0,255),plt.ylim(0,255)
plt.subplot(122)
plt.plot(curve2), plt.title('k=2')
plt.xlim(0,255),plt.ylim(0,255)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
