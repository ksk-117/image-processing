import cv2 
img = cv2.imread('pic/sample.pgm') 
cv2.namedWindow('img_test', cv2.WINDOW_NORMAL) 
cv2.imshow('img_test', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()