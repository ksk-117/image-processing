import cv2
import math
img = cv2.imread('pic/crescent.png', 0)
h, w = img.shape
print('h=', h, 'w=', w)
m = cv2.moments(img)
x_g = m['m10'] / m['m00']
y_g = m['m01'] / m['m00']
ang = 0.5 * math.atan2(2.0 * m['mu11'], m['mu20'] - m['mu02'])
print('x_g=', x_g, 'y_g=', y_g, 'ang=', math.degrees(ang))
cv2.line(img, (int(x_g - 500 * math.cos(ang)), int(y_g - 500 * math.sin(ang))), (int(x_g + 500 * math.cos(ang)), int(y_g + 500 * math.sin(ang))), 128, 1)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
