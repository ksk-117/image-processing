import cv2
cap = cv2.VideoCapture(0)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(w,h,fps)
codec = cv2.VideoWriter_fourcc(*'.mp4')
video = cv2.VideoWriter('output/output.mp4', codec, fps, (w,h))
while True:
    ret, img = cap.read()
    video.write(img)
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cap.release()
cv2.destroyAllWindows()
