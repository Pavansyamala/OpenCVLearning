'''
Low Pass Filters (LPF) --> Helps for removing Noise by blurring the image

High Pass Filters (HPF) --> Helps for finding edges in an image

Bilateral Filter --> Edges are Preserved in a Perfect Manner (No blurring of Edges will be present)
medianBlur --> Whenever there is a salt and pepper like noise is present then use medianBlur

'''
import cv2 
import numpy as np

img = cv2.imread('images/download (2).jpg')

kernal = np.ones((7,7))*(1/25)

dst = cv2.filter2D(img , -1 , kernal) ## Homogenous Filter 

blur = cv2.blur(img , (5,5))

gblur = cv2.GaussianBlur(img , (5,5) , 0)

mblur = cv2.medianBlur(img , 5)

bfilter = cv2.bilateralFilter(img , 9 , 75 , 75 )

cv2.imshow('Image' , img)
cv2.imshow('Homogenous' , dst)
cv2.imshow('Blurred Image' , blur)
cv2.imshow('Gaussian Blur' , gblur)
cv2.imshow('Median Blur' , mblur)
cv2.imshow('Bilater Filter' , bfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
