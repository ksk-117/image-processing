import cv2
img = cv2.imread('pic/Milkdrop.bmp')
cv2.imshow("img", img)
height = img.shape[0]
width = img.shape[1]
center = (int(width/2), int(height/2))
trans = cv2.getRotationMatrix2D(center, 45, 0.707)
dst = cv2.warpAffine(img, trans, (width, height))
cv2.imshow("dst 45", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
