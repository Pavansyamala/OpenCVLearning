import numpy as np
import cv2

img = np.zeros((10000,10000,3)) ## All are Zeros 
white_img = np.ones((1000,1000,3)) ## All are Ones 

## Drawing Line 
img = cv2.line(img , (0,0),(100,100) , (0,0,255) , 3 )
img = cv2.arrowedLine(img , (0,0),(100,100) , (0,0,255) , 3 )
img = cv2.rectangle(img,(105,105),(205,205),(0,255,0),-1)
img = cv2.circle(img , (305,305),100,(255,0,0),4)

cv2.imshow('Black Image' , img)
cv2.waitKey(10000)
cv2.destroyAllWindows()


