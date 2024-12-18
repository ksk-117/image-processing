import cv2
img = cv2.imread('pic/Pepper.bmp')
cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
dst_c = cv2.Canny(img, 80, 200)
dst_g80 = cv2.Canny(gray, 80, 200)
dst_g40 = cv2.Canny(gray, 40, 200)
cv2.imshow('dst_color80', dst_c)
cv2.imshow('dst_gray80', dst_g80)
cv2.imshow('dst_gray40', dst_g40)
cv2.waitKey(0)
cv2.destroyAllWindows()
