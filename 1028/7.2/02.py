import cv2
img = cv2.imread('pic/Mandrill.bmp', 0)
cv2.imshow('img', img)
dst = cv2.Laplacian(img, -1)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
