import cv2
img = cv2.imread('pic/flower01.jpg')
cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
cv2.imshow('th', thresh)
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
