import cv2
def nothing(x):
    pass
img = cv2.imread('pic/Mandrill.bmp')
cv2.imshow('img', img)
cv2.createTrackbar('Sigma', 'img', 1, 50, nothing)
while True:
    sigma = cv2.getTrackbarPos('Sigma', 'img')
    if sigma == 0:
        sigma = 1
    dst1 = cv2.GaussianBlur(img, (5, 5), sigma)
    dst2 = cv2.GaussianBlur(img, (7, 7), sigma)
    cv2.imshow('dst 5x5', dst1)
    cv2.imshow('dst 7x7', dst2)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()