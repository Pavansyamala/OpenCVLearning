import cv2 

image = cv2.imread("D:\WhatsApp Image 2023-08-13 at 13.58.12.jpeg" , 1) ## Reading Image 

## Saving the image when user clicks s only and when user clicks close window symbol then destroy the image and dont save it

cv2.imshow('Pavan Kasa' , image)
key = cv2.waitKey(0) ## if the system is 64 bit machine then use cv2.waitKey(0) & 0xFF

if key == 27 : ## Represents  clicks close window symbol 
    cv2.destroyAllWindows()
if key == ord('s'):
    cv2.imwrite(filename='pavan.png' , img=image) ## Writing image to pavan.png file 
    cv2.destroyAllWindows()   