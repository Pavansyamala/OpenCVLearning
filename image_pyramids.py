import cv2 
import numpy as np

img = cv2.imread('D:\\CV(OPENCV)\\images\\download.jpg') 
img = cv2.resize(img , (88,142))

sd = cv2.pyrDown(img)
su = cv2.pyrUp(img) 
ssd = cv2.pyrDown(su)

layer = img.copy()
GaussianPyramids = [layer] 

for i in range(6):
    layer = cv2.pyrDown(layer) 
    print(layer.shape)
    GaussianPyramids.append(layer) 
    # cv2.imshow(str(i) , layer) 

print(len(GaussianPyramids))
'''
Laplacian Pyramid :  
image at ith position is given by (GaussianPyramid[i] - pyrUp(GuassianPyramid[i+1]))
'''
layer = GaussianPyramids[-1]
laplacianPyramids = [layer] 

for i in range(5,0,-1):
    ge = cv2.pyrUp(GaussianPyramids[i]) 
    print(ge.shape)
    lpi = cv2.subtract(GaussianPyramids[i-1] , ge) 
    laplacianPyramids.append(lpi) 
    cv2.imshow(str(i) , lpi)

cv2.imshow('Image' , img)
cv2.imshow('Scale Up' , su)
cv2.imshow('Scale Down' , sd)
cv2.imshow('Scale Down After Scale Up' , ssd)
cv2.waitKey(0)
cv2.destroyAllWindows()
