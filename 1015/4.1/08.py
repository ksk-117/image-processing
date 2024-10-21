import cv2
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('img', img)
SCSLE = 0.2
h, w, c = img.shape
dst = cv2.resize(img, (round(w * SCSLE), round(h * SCSLE)))
dst = cv2.resize(dst, (w, h), cv2.INTER_NEAREST)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()