import cv2
img = cv2.imread('pic/Sailboat.bmp')
cv2.imshow('img', img)
height = img.shape[0]
width = img.shape[1]
dst  = img[170:height-20, 128:width-64]
cv2.imwrite('pic/Trimming.jpg', dst)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()