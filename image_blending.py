import cv2 
import numpy as np 

img1 = cv2.imread('images/WhatsApp Image 2023-08-19 at 06.55.06.jpeg')
img2= cv2.imread('images/WhatsApp_Image_2023-08-13_at_13.58.12-removebg-preview (1).png')  

cv2.imshow('Image 1 ' , img1)
cv2.imshow('Image 2 ', img2)

print(img1.shape, img2.shape)

'''

img1_ = img1[:, :190]
img2_ = img2[:,190:]

stacked = np.hstack((img1_,img2_))

cv2.imshow('Stacked Image' , stacked)

Drawback of this method is the line of splitting is clearly visible and thick , so when we are trying to find edge detection then this will affect
our requirements and that line will be detected 

'''
layer = img1.copy()
gp_img1 = [layer] 

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp_img1.append(layer) 

layer = img2.copy()
gp_img2 = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp_img2.append(layer)

## Now finding the laplacian pyramids corrosponding to the gaussian pyramids 
layer1 = gp_img1[-1]
layer2 = gp_img2[-1]
lp_img1 = [layer1]
lp_img2 = [layer2] 

for i in range(6,0,-1):
    ge_img1 = cv2.pyrUp(gp_img1[i])
    ge_img1 = cv2.resize(ge_img1, gp_img1[i-1].shape[:2][::-1])  # Resize ge to match the dimensions
    lpi = cv2.subtract(gp_img1[i-1], ge_img1)
    lp_img1.append(lpi) 

    ge_img2 = cv2.pyrUp(gp_img2[i])
    ge_img2 = cv2.resize(ge_img2, gp_img2[i-1].shape[:2][::-1])  # Resize ge to match the dimensions
    lpi_2 = cv2.subtract(gp_img2[i-1], ge_img2)
    lp_img2.append(lpi_2)

req_pyr = [] 

for im1_ , im2_ in zip(lp_img1,lp_img2):
    rows , cols = im1_.shape[:2]
    lp_stacked = np.hstack((im1_[:,:cols//2] , im2_[:,cols//2 : ]))
    req_pyr.append(lp_stacked) 

## Reconstructing the image 
reconstructed = req_pyr[0]
for i in range(1,len(req_pyr)):
    reconstructed = cv2.pyrUp(reconstructed)
    print('After ' , reconstructed.shape , req_pyr[i].shape)
    reconstructed = cv2.resize(reconstructed, req_pyr[i].shape[:2][::-1])
    print('Before ' , reconstructed.shape , req_pyr[i].shape)
    reconstructed = cv2.add(req_pyr[i] , reconstructed) 
    cv2.imshow(str(i) , reconstructed)


cv2.imshow('Stacked' , reconstructed)

cv2.waitKey(0)
cv2.destroyAllWindows()
