import cv2
img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")
if img is None:
    print("Error: image not find")
else:
    center=(140,90)
    radius=(49)
    color=(0,0,255)
    thickness=3
    thicknes_full=-1#complete fill
    cv2.circle(img,center,radius,color,thickness)
    cv2.imshow("circle",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()