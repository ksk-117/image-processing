import cv2
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('img', img)
dst1 = cv2.GaussianBlur(img, (5,5), 3)
dst2 = cv2.GaussianBlur(img, (7,7), 3)
cv2.imshow('dst 5*5 s=3', dst1)
cv2.imshow('dst 7*7 s=3', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
