import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\\CV(OPENCV)\\images\\download.jpg',0)
_,ths1 = cv2.threshold(img , 200 , 255 , cv2.THRESH_BINARY_INV)
kernal = np.ones((5,5))
dilated = cv2.dilate(img , kernal , iterations=3) ## Dilation Method 
eroted = cv2.erode(ths1 , kernal , iterations=2)
close = cv2.morphologyEx(ths1 , cv2.MORPH_CLOSE , kernal)
opened = cv2.morphologyEx(ths1 , cv2.MORPH_OPEN , kernal)
gradient = cv2.morphologyEx(ths1 , cv2.MORPH_GRADIENT , kernal)
black_hat = cv2.morphologyEx(ths1 , cv2.MORPH_BLACKHAT , kernal)
top_hat = cv2.morphologyEx(ths1 , cv2.MORPH_TOPHAT , kernal)

cv2.imshow('Image' , img) 
cv2.imshow('Image1' , ths1)
cv2.imshow('Dilated' , dilated)
cv2.imshow('Eroted' , eroted)
cv2.waitKey(0)
cv2.destroyAllWindows()
