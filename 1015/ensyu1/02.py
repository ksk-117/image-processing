import cv2
img = cv2.imread('pic/Mandrill.bmp')
cv2.putText(img, 'Mandrill', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 6)
cv2.putText(img, 'Mandrill', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imwrite('Title.jpg', img)
cv2.imshow('Title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()