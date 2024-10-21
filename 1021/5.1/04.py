import cv2 
import matplotlib.pyplot as plt 
import numpy as np
def negaposi():
    curve = 255- np.arange(0, 256)
    return curve.astype(np.uint8)
src = cv2.imread('pic/Mandrill.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)
curve = negaposi()
dst = cv2.LUT(src, curve)
cv2.imshow('dst', dst)
plt.plot(curve), plt.title('negaposi')
plt.xlim(0,255),plt.ylim(0,255)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

