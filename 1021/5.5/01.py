import cv2
img = cv2.imread('pic/Parrots.bmp')
flip_img = cv2.flip(img, 1)
hconcat_img = cv2.hconcat([img, flip_img])
cv2.imshow("img", img)
cv2.imshow("flip_img", flip_img)
cv2.imshow("hconcat_img", hconcat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
