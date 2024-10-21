import cv2
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('img', img)
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('dst_gray.jpg', dst)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWondows()