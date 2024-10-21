import cv2
img = cv2.imread('Mandrill.bmp')
cv2.imshow('src', img)
h, w, c = img.shape
print(h, w, c)
img_resize = cv2.resize(img, (round(w * 2.5),h), cv2.INTER_LINEAR)
cv2.imshow('dst_linear', img_resize)
img_resize = cv2.resize(img, (round(w * 2.5),h), cv2.INTER_NEAREST)
cv2.imshow('dst_nearest', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()