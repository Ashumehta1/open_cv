import cv2
img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")
if img is None:
    print("Error: could not read pic")
else:
    cv2.putText(img,"Shri Radhe Radhe",(10,150),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255),1)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()