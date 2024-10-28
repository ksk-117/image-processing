import cv2
img = cv2.imread('pic/Aerial.bmp')
cv2.imshow('img', img)
dst_80 = cv2.Canny(img, 80, 200)
cv2.imshow('dst_80', dst_80)
cv2.waitKey(0)
cv2.destroyAllWindows()
