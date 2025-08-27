# ask path of image from user to load then ask what to draw from user also take requirements from user to draw
# then save
import cv2
img_path=input("Enter path to load pic: ")
img=cv2.imread(img_path)
selection =int(input("Enter 0 or 1 or 2 to draw line or rectangle or circle: "))
img_path_write=input("Enter file name with .jpg or .png: ")

def draw_line():
    pt1 = tuple(map(int, input("Enter starting coordinate (x,y): ").split(',')))
    pt2 = tuple(map(int, input("Enter end coordinate (x,y): ").split(',')))
    color=tuple(map(int, input("Enter BGR CODE FOR COLOR:").split(',')))
    thickness=int(input("Enter thickness of line: "))
    cv2.line(img,pt1,pt2,color,thickness)
    return img

def draw_rectangle():
    pt1 = tuple(map(int, input("Enter starting coordinate (x,y): ").split(',')))
    pt2 = tuple(map(int, input("Enter end coordinate (x,y): ").split(',')))
    color=tuple(map(int, input("Enter BGR CODE FOR COLOR:").split(',')))
    thickness=int(input("Enter thickness of rectangle: "))
    cv2.rectangle(img,pt1,pt2,color,thickness)
    return img

def draw_circle():
    cente = tuple(map(int, input("Enter center coordinate (x,y): ").split(',')))
    radius = int(input("Enter end radius (x): "))
    color=tuple(map(int, input("Enter BGR CODE FOR COLOR:").split(',')))
    thickness=int(input("Enter thickness of circle: "))
    cv2.circle(img,cente,radius,color,thickness)
    return img

if selection==0:
    image=draw_line()
elif selection==1:
    image=draw_rectangle()
elif selection==2:
    image=draw_circle()
    
cv2.imwrite(img_path_write,img)
cv2.imshow("draw",image) 
cv2.waitKey(0)
cv2.destroyAllWindows()