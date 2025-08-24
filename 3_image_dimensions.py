import cv2
image=cv2.imread("my_pic.png")
if image:
    h,w,c=image.shape
    print("image dimensions: \nheight:{h}\nwidth:{w}\nchanel:{c}")
else:
    print("error: image not loaded")