import cv2
img=img=cv2.imread("D:\project\myPproject\Open_cv\krishna.jpg")
if img is None:
    print("Image not find")
else:
    (h,w) = img.shape[:2]
    m=cv2.getRotationMatrix2D((w//2,h//2),70,1)
    rotated_img=cv2.warpAffine(img,m,(w*2,h*2))
    cv2.imshow("Original",img)
    cv2.imshow("rotated",rotated_img)
    cv2.waitKey(0)
    cv2.destroyedAllwindow()