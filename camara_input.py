import cv2 

## Capturing Live Stream from Camera 

cap = cv2.VideoCapture(0)  
## provide 0 for reading from camara 1 , 1 for reading from camera2 , and so on..... , if we want to read from file then provede file path as a argument

## For Capturing frame Continuosly 

print(cap.isOpened()) ## Provides is the file or camera opened it opens it will return True otherwise it will return False 

'''
        cap.isOpened() use this in the while loop instead of using True as if we use true and video is not opened then it will return raise error 
        For avoiding the error use it inplace of True 

        while cap.isOpened() :
            ret , frame = cap.read() ## Return True,frame if frame is present 
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ## For converting the frame into Gray Color 
            cv2.imshow('PavanKasa' , gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
            break


'''

while True:
    ret , frame = cap.read() ## Return True,frame if frame is present 
    if not ret:       ## Checking that is the ret true of False if it is False then there is no Frame returned so break the loop
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ## For converting the frame into Gray Color 
    cv2.imshow('PavanKasa' , gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

## releasing Capture value 
cap.release()
cv2.destroyAllWindows()

'''
    for getting frame width , frame height use 
    cap.get(cv2.CAP_PROP_FRAME_WIDTH) ## for width 
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT) ## for Height 

'''