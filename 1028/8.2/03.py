import cv2
def nothing(x):
    pass
img = cv2.imread('pic/flower02.jpg')
cv2.imshow('img', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)
cv2.createTrackbar('H-Low', 'HSV', 0, 179, nothing)
cv2.createTrackbar('S-Low', 'HSV', 0, 255, nothing)
cv2.createTrackbar('V-Low', 'HSV', 0, 255, nothing)
cv2.createTrackbar('H-Up', 'HSV', 179, 179, nothing)
cv2.createTrackbar('S-Up', 'HSV', 255, 255, nothing)
cv2.createTrackbar('V-Up', 'HSV', 255, 255, nothing)
while True:
    if cv2.waitKey(1) == ord('q'):
        break
    HL = cv2.getTrackbarPos('H-Low', 'HSV')
    SL = cv2.getTrackbarPos('S-Low', 'HSV')
    VL = cv2.getTrackbarPos('V-Low', 'HSV')
    lower = (HL, SL, VL)
    HU = cv2.getTrackbarPos('H-Up', 'HSV')
    SU = cv2.getTrackbarPos('S-Up', 'HSV')
    VU = cv2.getTrackbarPos('V-Up', 'HSV')
    upper = (HU, SU, VU)
    bin_img = cv2.inRange(hsv, lower, upper)
    cv2.imshow('HSV', bin_img)
cv2.destroyAllWindows()
