import cv2 

img1 = cv2.imread("D:\\CV(OPENCV)\\images\\WhatsApp Image 2023-08-13 at 13.58.12.jpeg")
img2 = cv2.imread("D:\\CV(OPENCV)\\images\\WhatsApp Image 2023-08-19 at 06.55.06.jpeg")

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1 , (500,500)) ## reshaping 1st image to the same size
combined = cv2.add(img1,img2)     ## adding 2 images 
cv2.imshow('Added Image ' , combined)

'''
 Giving Certain Weights to each of the images like i want to give 90% importance to 1st image and 10% importance
to second image then the following method can be used '''


resultant = cv2.addWeighted(img1 , 0.7 , img2 , 0.3 , 0)

cv2.imshow('Weighted Image ' , resultant)

cv2.waitKey(0)
cv2.destroyAllWindows()
