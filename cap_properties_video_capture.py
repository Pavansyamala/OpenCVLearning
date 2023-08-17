import cv2 

cap = cv2.VideoCapture(0) 

while cap.isOpened():

    ret , frame = cap.read()
    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('Kasa Pavan' , frame)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break 

'''
cap --> it has a 2 attributes get and set through wich we can get the properties of the image and set the properties of the image

1. get() ->    Used for Getting the Properties of Image 
    \ Below Properties are used for both Cameras and already existing Videos in the System
    . cap.get(cv2.CAP_PROP_FRAME_WIDTH) ## used for getting the width of the frame
    . cap.get(CV2.CAP_PROP_FRAME_HEIGHT) ## used for getting the height of the frame 
    . cap.get(CV2.CAP_PROP_FPS) ## used for getting the number of frames per second
    . cap.get(cv2.CAP_PROP_FRAME_COUNT) ## Used for Getting the Number of Frames per Second
    \ Below Properties are used only for Cameras not for the alredy existing video in the system
    . cap.get(cv2.CAP_PROP_BRIGHTNESS) ## For Getting the Brightness of the image        
    . cap.get(cv2.CAP_PROP_CONTRAST)
    . cap.get(cv2.CAP_PROP_SATURATION)
    . cap.get(cv2.CAP_PROP_HUE)
    . cap.get(cv2.CAP_PROP_GAIN) ## Gain of the image
    . cap.get(cv2.CAP_PROP_EXPOSURE) ## exposure of the image

'''