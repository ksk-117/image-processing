import cv2
def nothing(s):
    pass
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('img', img)
cv2.createTrackbar('V-Up', 'HSV', 255, 255, nothing)
while True:
    if cv2.waitKey(1) == ord('q'):
        break
s = cv2.getTrackbarPos('s', 's')
dst1 = cv2.GaussianBlur(img, (5,5), s)
dst2 = cv2.GaussianBlur(img, (7,7), s)
cv2.imshow('dst 5*5 s=3', dst1)
cv2.imshow('dst 7*7 s=3', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()