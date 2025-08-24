import cv2
img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")

if img is not None:
    croped=img[100:150,100:150]
    cv2.imshow("original",img)
    cv2.imshow("croped",croped)
    cv2.waitKey(0)
    cv2.destroyedAllwindows()
else:
    print("Error: image not find")