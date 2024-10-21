import cv2
img = cv2.imread('pic/Parrots.bmp')
cv2.imshow("img", img)
height = img.shape[0]
width = img.shape[1]
center = (int(width/2), int(height/2))
trans = cv2.getRotationMatrix2D(center, 30.0, 1.0)
dst = cv2.warpAffine(img, trans, (width, height))
cv2.imshow("dst 30", dst)
trans = cv2.getRotationMatrix2D(center, 60.0, 0.73)
dst = cv2.warpAffine(img, trans, (width, height), flags=cv2.INTER_CUBIC)
cv2.imshow("dst 60", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
