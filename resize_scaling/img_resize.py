import cv2
img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")

if img is not None:
    img_resize=cv2.resize(img,(500,600))
    cv2.imshow("original",img)
    cv2.imshow("resized",img_resize)
    cv2.waitKey(0)
    cv2.destroyedAllwindows()
else:
    print("Error: image coul not loaded")