import cv2
img = cv2.imread('pic/Kitazato.jpg')
cv2.imshow('src', img)
print(img.shape)
img_resize = cv2.resize(img, (800, 600))
cv2.imshow('dst', img_resize)
cv2.imwrite('pic/kitazato.bmp', img_resize)
cv2.waitKey(0)
cv2.destroyAllWondows()