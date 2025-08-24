import cv2
image_color=cv2.imread("krishna.jpg",1)#colour
image_gray=cv2.imread("krishna.jpg",0)#gray
image_same=cv2.imread("krishna.jpg",-1)#no change
if image_same is not None:
    cv2.imshow("krishna",image_same)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error:image not find")

