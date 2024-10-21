import cv2
img = cv2.imread('pic/Airplane.bmp')
cv2.imshow('img', img)
height = img.shape[0]
width = img.shape[1]
dst  = img[20:height-20, 20:width-20]
cv2.imwrite('pic/Trimming.jpg', dst)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()