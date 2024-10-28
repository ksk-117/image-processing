import cv2
img = cv2.imread('pic/noise_color.bmp')
cv2.imshow('img', img)
dst1 = cv2.medianBlur(img, 3)
dst2 = cv2.medianBlur(img, 9)
cv2.imshow('dst 3*3', dst1)
cv2.imshow('dst 9*9', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
