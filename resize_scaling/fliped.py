import cv2
img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")
if img is None:
    print("could not load imgage")
else:
    img_vertical=cv2.flip(img,0)
    img_horizontal=cv2.flip(img,1)
    img_both=cv2.flip(img,-1)
    cv2.imshow("original",img)
    cv2.imshow("img_vertical",img_vertical)
    cv2.imshow("img_horizontal",img_horizontal)
    cv2.imshow("img_both",img_both)
    cv2.waitKey(0)
    cv2.destroyAllWindow()