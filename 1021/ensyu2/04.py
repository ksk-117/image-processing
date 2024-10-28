import cv2
import numpy as np
img = cv2.imread('pic/Kitazato.bmp')
cv2.imshow("original", img)
h, w, c = img.shape
src_pts = np.array([[0, 0], [0, h], [w, h], [w, 0]], dtype=np.float32)
dst_pts = np.array([[-240, -530],[-75, h+140],[w-50, h+185],[w+110,-280]], dtype=np.float32)
perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
dst = cv2.warpPerspective(img, perspective_matrix, (w, h))
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
