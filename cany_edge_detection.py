'''
Cany Edge Detection consists of mainly 5 composed steps 

1. Noise Reduction 
2. Gradient Calculation 
3. Non Maimum Supression 
4. Double Threshold 
5. Edge Tracking by Hysterysis

'''


import cv2 
import numpy as np

img = cv2.imread('images/download.png')

canny = cv2.Canny(img , 100 , 200 )

cv2.imshow('Image' , img)
cv2.imshow('Canny' , canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
