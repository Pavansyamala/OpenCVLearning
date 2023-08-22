
'''
Image Gradients are the directional change in the intensity or color of an image 

3 Main Gradient Mehods are : 
    1) Laplacian Derivative 
    2) Sobal X 
    3) sobal Y

'''

import cv2 
import numpy as np

img = cv2.imread('images/download.png')

lap = cv2.Laplacian(img , cv2.CV_64F )

lap1 = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img , cv2.CV_64F , 1 , 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = cv2.Sobel(img , cv2.CV_64F , 0 , 1)
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX , sobelY)

cv2.imshow('Image' , img)
# cv2.imshow('Lap' , lap)
cv2.imshow('Laplacian' , lap1)
cv2.imshow('Sobel X', sobelX)
cv2.imshow('Sobel Y' , sobelY)
cv2.imshow('Sobel' , sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
