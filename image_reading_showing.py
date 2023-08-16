import cv2 

image = cv2.imread("D:\WhatsApp Image 2023-08-13 at 13.58.12.jpeg" , 1) ## Reading Image 
image1 = cv2.imread("D:\WhatsApp Image 2023-08-13 at 13.58.12.jpeg" , -1) 
## Flag : 0 --> for Gray scale Image and Flag : 1 --> For Coloured Image  , Flag : -1 --> For displaying image as it is 
print(image) ## Prints the pixels of image 

## Displaying Image 

cv2.imshow('Pavan Kasa' , image)  ## Opens the Window with Pavan Kasa and Displays image in this window and it will appear for 1 ms and then disappear
cv2.imshow('Pavan Kasa_' , image1) 
cv2.waitKey(10000) ## No.of milli seconds you want to show the window 
# if we will pass 0 in WaitKey method then it will wait until we closed it so give 0 if you want to give 
cv2.destroyAllWindows() ## Destroys all windows which we have creted during 

