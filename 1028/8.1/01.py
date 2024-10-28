import cv2
img = cv2.imread('pic/crescent.png',0)
cv2.imshow('img', img)
x, y, w, h = cv2.boundingRect(img)
aspectratio = float(h)/w
print(aspectratio)
cv2.rectangle(img, (x, y), (x + w, y + h), 170)
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
