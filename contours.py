import cv2 
import numpy as np 

img_ = cv2.imread('images/opencv_image.png')
img = cv2.cvtColor(img_ , cv2.COLOR_BGR2GRAY)

cv2.imshow('Image' , img_)

ret , thresh = cv2.threshold(img , img.max()//2 + 10 , img.max() , 0)
ret , thresh1 = cv2.threshold(img , img.max()//2 + 10 , img.max() , cv2.THRESH_BINARY_INV)
contours , hierarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
print(len(contours))
print(contours)
img = cv2.drawContours(img_ , contours , -1 , (0,22,255) , 3)
cv2.imshow('Contours Image' , img)
cv2.imshow('Thresh' , thresh)
cv2.imshow('Thresh_inv' , thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()
