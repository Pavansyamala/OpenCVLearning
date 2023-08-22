import matplotlib.pyplot as plt 
import numpy as np
import cv2 

img = cv2.imread('D:\\CV(OPENCV)\\images\\WhatsApp Image 2023-08-13 at 13.58.12.jpeg')
img = cv2.resize(img,(500,500))
# cv2.imshow('Image' , img)
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([])  ## For Removing the ticks on x-axis
plt.yticks([])  ## For Removing the ticks on y-axis
plt.show()

'''
Shoeing Multiple Images in One Plot
''' 
a = np.max(img)
_ , ths1 = cv2.threshold(img , a//2 , a , cv2.THRESH_BINARY)
_ , ths2 = cv2.threshold(img , a//2 , a , cv2.THRESH_BINARY_INV)

j = 1
for i in [img , ths1 , ths2]:
    plt.subplot(2,2,j)
    plt.imshow(i)
    j += 1 
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
