'''
Whenever in the image from pixel to pixel contains varying illumination, simple thresholding doesnt work so we need to use adaptive thresholding 
in this case

In adaptive thresholding, the thresholding level is not fixed; it will be calculated locally based on the surrounding regions 

'''

import cv2 

import numpy as np

image = cv2.imread("D:\\CV(OPENCV)\\images\\WhatsApp Image 2023-08-13 at 13.58.12.jpeg" , 0)
image = cv2.resize(image , (500,500))

a = np.max(image) 

bin = cv2.adaptiveThreshold(image , a , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 2)
gauss = cv2.adaptiveThreshold(image , a , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2)

cv2.imshow('Image' , image)
cv2.imshow('Binary ' , bin)
cv2.imshow('Gaussian ' , gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
