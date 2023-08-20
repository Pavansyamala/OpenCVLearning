import cv2
import numpy as np

def update_blue_value(value):
    pass 

# Create a black image
img = np.zeros((300, 500, 3), dtype=np.uint8)

cv2.namedWindow('Tracking')

# Create a trackbar named 'Blue' that goes from 0 to 255
cv2.createTrackbar('LH', 'Tracking', 0, 255, update_blue_value)
cv2.createTrackbar('LS', 'Tracking', 0, 255, update_blue_value)
cv2.createTrackbar('LV', 'Tracking', 0, 255, update_blue_value)

cv2.createTrackbar('UH', 'Tracking', 255, 255, update_blue_value)
cv2.createTrackbar('US', 'Tracking', 255, 255, update_blue_value)
cv2.createTrackbar('UV', 'Tracking', 255, 255, update_blue_value)



while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
