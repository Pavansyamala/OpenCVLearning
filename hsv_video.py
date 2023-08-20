import cv2 

import numpy as np

def update_blue_value(value):
    pass 

cv2.namedWindow('Tracking')

# Create a trackbar named 'Blue' that goes from 0 to 255
cv2.createTrackbar('LH', 'Tracking', 0, 255, update_blue_value)
cv2.createTrackbar('LS', 'Tracking', 0, 255, update_blue_value)
cv2.createTrackbar('LV', 'Tracking', 0, 255, update_blue_value)

cv2.createTrackbar('UH', 'Tracking', 255, 255, update_blue_value)
cv2.createTrackbar('US', 'Tracking', 255, 255, update_blue_value)
cv2.createTrackbar('UV', 'Tracking', 255, 255, update_blue_value)


video = cv2.VideoCapture(0)

while video.isOpened() :

    ret , img = video.read() 

    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    cv2.COLOR_HSV2BGR

    l_h = cv2.getTrackbarPos('LH','Tracking')
    l_s = cv2.getTrackbarPos('LS','Tracking')
    l_v = cv2.getTrackbarPos('LV','Tracking')

    u_h = cv2.getTrackbarPos('UH','Tracking')
    u_s = cv2.getTrackbarPos('US','Tracking')
    u_v = cv2.getTrackbarPos('UV','Tracking')

    l_b = np.array([l_h,l_s,l_v]) ## For lower_blue_color_range
    u_b = np.array([u_h,u_s,u_v]) ## Upper Limit for Blue Color

    mask = cv2.inRange(hsv , l_b , u_b)

    res = cv2.bitwise_and(img , img , mask=mask)

    cv2.imshow('Image' , img) 
    cv2.imshow('Result ' , res)
    cv2.imshow('mask' , mask)
    cv2.imshow('hsv' , hsv)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break 

video.release()
cv2.destroyAllWindows()
