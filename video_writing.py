import cv2 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  ## *XVID is the fourcc code 
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))

'''
 0-> 1st camera of your sysytem , fourcc -> fourcc variable of videowriter , 20.0 -> 20 frames per second we need 
 (640,480) -> Shape of the output image
'''

while cap.isOpened():
    ret , frame = cap.read()

    if ret == True :

        out.write(frame)

        cv2.imshow('Pavan Kasa' , frame) 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
out.release()
cap.release()
cv2.destroyAllWindows() 
