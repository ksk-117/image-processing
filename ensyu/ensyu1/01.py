import cv2
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('pic/img.bmp', img)
cv2.imwrite('pic/Mandrill.jpg', img)
cv2.imshow('pic/img.jpg', img)
cv2.imwrite('pic/Mandrill.png', img)
cv2.imshow('pic/img.png', img)
cv2.imwrite('pic/Mandrill.tif', img)
cv2.imshow('pic/img.tif', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
