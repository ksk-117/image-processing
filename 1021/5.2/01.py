import cv2
img = cv2.imread("pic/Parrots.bmp")
cv2.imshow("img", img)
dst = cv2.flip(img, 0)
#cv2.imwrite("pic/flip0.jpg, dst")
cv2.imshow("dst 0", dst)
dst = cv2.flip(img, 1)
cv2.imshow("dst 1", dst)
dst = cv2.flip(img, -1)
cv2.imshow("dst -1", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
