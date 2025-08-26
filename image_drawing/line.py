import cv2
img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")
if img is None:
    print("Error: image could not loaded")
else:
    pt1=(30,40)
    pt2=(100,200)
    color=(0,255,0)
    thickness=4
    img_line=cv2.line(img,pt1,pt2,color,thickness)
    cv2.imshow("original",img)
    cv2.imshow("with_line",img_line)
    cv2.waitKey(0)
    cv2.destroyAllwindows()