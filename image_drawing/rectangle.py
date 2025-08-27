import cv2
img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")
if img is None:
    print("Error: Img not find")
else:
    print(img.shape)
    pt1=(60,50)
    pt2=(160,100)
    color=(0,0,255)
    thickness=4
    cv2.rectangle(img,pt1,pt2,color,thickness)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()