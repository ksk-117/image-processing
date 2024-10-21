import cv2
img1 = cv2.imread('pic/Parrots.bmp')
img2 = cv2.imread('pic/Mandrill.bmp')
vconcat_img = cv2.vconcat([img1, img2])
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("vconcat_img", vconcat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
