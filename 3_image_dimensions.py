import cv2
image_=cv2.imread("krishna.jpg",0)
if image_ is not None:
    if len(image_.shape) == 2:
        h,w=image_.shape
        c=1
    else:
        h, w, c = image_.shape
    print(f"image dimensions: \nheight:{h}\nwidth:{w}\nchanel:{c}")
    cv2.imshow("pic",image_)
    cv2.waitKey(0)
    cv2.destroyAllwindow()
else:
    print("Error: image not loaded")