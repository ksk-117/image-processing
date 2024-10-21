import cv2
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('src', img)
print(img.shape)
img_resize = cv2.resize(img, (200, 200))
cv2.imshow('dst', img_resize)
cv2.waitKey(0)
cv2.destroyAllWondows()