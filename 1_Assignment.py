#load image-->convert into gray scale--> ask window name from user to show-->ask file name --> save
import cv2
img=cv2.imread("my_pic.png")
if img is not None:
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    window_name=input("Enter window name: ")
    cv2.imshow(window_name,img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    file_name=input("Enter file name to save(with extension, e.g., photo.png): ")
    if not (file_name.endswith(".png") or file_name.endswith(".jpg")):
        file_name+=".png"
    success=cv2.imwrite(file_name,img_gray)
    if success:
        print("File successfuly saved")
    else:
        print("error while saving")

else:
    print("Error: Img not find")