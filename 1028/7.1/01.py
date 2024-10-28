import cv2
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('img', img)
dst1 = cv2.blur(img, (3,3))
dst2 = cv2.Gausslur(img, (7,7), 0)
cv2.imshow('dst 3*3', dst1)
cv2.imshow('dst 7*7', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
