import cv2
import numpy as np
img = cv2.imread('pic/Parrots.bmp')
cv2.imshow("img", img)
h, w, c = img.shape
src_pts = np.array([[0, 0], [0, h], [w, h], [w, 0]], dtype=np.float32)

#pattern-0
dst_pts = np.array([[20, 10],[10, h-20],[w-20, h-30],[w-40, 30]], dtype=np.float32)
perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
dst = cv2.warpPerspective(img, perspective_matrix, (w, h))
cv2.imshow("dst 0", dst)

#pattern-1
h_margin = h/8
w_margin = w/8
dst_pts = np.array([[w_margin, h_margin],src_pts[1],src_pts[2],[w-w_margin, h_margin]], dtype=np.float32)
perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
dst = cv2.warpPerspective(img, perspective_matrix, (w, h))
cv2.imshow("dst 1", dst)

#pattern-2
h_margin = h/5
w_margin = w/5
dst_pts = np.array([src_pts[0],src_pts[1],[w-w_margin, h-h_margin],[w-w_margin, h_margin]], dtype=np.float32)
perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
dst = cv2.warpPerspective(img, perspective_matrix, (w, h))
cv2.imshow("dst 2", dst)

#pattern-3
h_margin = h/3
w_margin = w/3
dst_pts = np.array([[w_margin, h_margin],src_pts[1],[w-w_margin, h-h_margin],src_pts[3]], dtype=np.float32)
perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
dst = cv2.warpPerspective(img, perspective_matrix, (w, h))
cv2.imshow("dst 3", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
