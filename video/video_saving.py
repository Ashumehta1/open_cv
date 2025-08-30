import cv2
camera=cv2.VideoCapture(0)#use same camera of laptop
frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec=cv2.VideoWriter_fourcc(*'mp4v')
record=cv2.VideoWriter("myvideo.mp4",codec,0,(frame_width,frame_height))
while True:
    success, image=camera.read()
    if not success:
        break
    record.write(image)
    cv2.imshow("live",image)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        break
camera.release()
record.release()
cv2.distroyAllWindows()

