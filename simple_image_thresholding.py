'''

Image Thresholding Means Dividing Images exactly into the two regions where one region with less than the provided threshold 
and other region with the the threshold value greater than the provided threshold 

cv2.THRESH_BINARY ---> Whenever threshold value greater than the provided threshold value rounded off to maximum value other wise rounded to zero
cv2.THRESH_BINARY_INV --> Exact Opposite to the THRESH_BINARY
cv2.THRESH_TRUNC --> Whenever threshold value greter than provided threshold value then its rounded to threshold other wise it remains same
cv2.THRESH_TOZERO --> whenever pixel value < threshold its rounded to zero else its remains same 
cv2.THRESH_TOZERO_INV --> exact opposite to tozer
cv2.THRESH_MASK -->
'''

import cv2 
import numpy as np

image = cv2.imread("D:\\CV(OPENCV)\\images\\WhatsApp Image 2023-08-13 at 13.58.12.jpeg")
image = cv2.resize(image , (500,500))
a = np.max(image)
ret , binary = cv2.threshold(image , a//2 , a , cv2.THRESH_BINARY)
ret , inv_binary = cv2.threshold(image , a//2 , a , cv2.THRESH_BINARY_INV)
ret , trunc = cv2.threshold(image , a//2 , a , cv2.THRESH_TRUNC)
ret , tozero = cv2.threshold(image , a//2 , a , cv2.THRESH_TOZERO)
ret , tozero_inv = cv2.threshold(image , a//2 , a , cv2.THRESH_TOZERO_INV) 
ret , mask = cv2.threshold(image , 10 , a , cv2.THRESH_MASK)

cv2.imshow('Image ' , image)
cv2.imshow('Binary ' , binary)
cv2.imshow('Inverse Binary ',inv_binary)
cv2.imshow('Trunc ' , trunc)
cv2.imshow('To Zero ' , tozero)
cv2.imshow('To Zero Inv ' , tozero_inv)
cv2.imshow('Mask' , mask)
cv2.waitKey(0) 

cv2.destroyAllWindows()
