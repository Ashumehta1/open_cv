import cv2
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read() #ret=true/false, frame=image
    if not ret:
        print("Could not capture video")
        break
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Exit")
        break
cap.release()
cv2.destroyAllWindows()



