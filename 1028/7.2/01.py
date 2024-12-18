import cv2
img = cv2.imread('pic/Mandrill.bmp', 0)
cv2.imshow('img', img)
dstx = cv2.Sobel(img, -1, 1, 0)
dsty = cv2.Sobel(img, -1, 0, 1)
dstxy = cv2.add(dstx, dsty)
cv2.imshow('dstx', dstx)
cv2.imshow('dsty', dsty)
cv2.imshow('dstxy', dstxy)
cv2.waitKey(0)
cv2.destroyAllWindows()
