import cv2
img = cv2.imread('pic/Pepper.bmp')
cv2.imshow('img', img)
img[20:50, 50:200] = 0
cv2.imshow('dst1', img)
img[20:50, 50:200] = [255, 0, 0]
cv2.imshow('dst2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()