'''

let's say if we have common in 2 images and we want that common part only and remaining thing will be some color then use bitwise_and
let's say if we have  2 images and we want that all the parts which are present in either image1 or imag2 then use bitwise_or
let's say if we have one images and we want to flip the image like the values 0 to 1 or 1 to 0 then use bitwise_not

like consider 1-> white portion and 0->black portion then 
if we want the region which is present in image1 or image2 but not present in both or absent in both then use bitwise_xor

'''
import cv2

img1 = cv2.imread("D:\\CV(OPENCV)\\images\\WhatsApp Image 2023-08-13 at 13.58.12.jpeg")
img2 = cv2.imread("D:\\CV(OPENCV)\\images\\WhatsApp Image 2023-08-19 at 06.55.06.jpeg")

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1 , (500,500))
img2 = cv2.resize(img2 , (500,500))

print(img1.shape)
print(img2.shape)

bitwise_and = cv2.bitwise_and(img1,img2)
bitwise_or = cv2.bitwise_or(img1,img2)
bitwise_xor = cv2.bitwise_xor(img1,img2)
bitwise_not = cv2.bitwise_not(img1)

cv2.imshow('image 1' , img1)
cv2.imshow('image 2', img2)

cv2.imshow('bitwise and ' , bitwise_and)
cv2.imshow('bitwise or' , bitwise_or)
cv2.imshow('bitwise xor' , bitwise_xor)
cv2.imshow('bitwise not' , bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
