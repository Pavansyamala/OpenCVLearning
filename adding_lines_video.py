 import cv2
import datetime

cap = cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 1080)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1080)


while cap.isOpened():

    ret , frame = cap.read()
    cv2.rectangle(frame,(0,110),(350,50),(0,255,0),4)
    text = 'Time is  : ' + str(datetime.datetime.now())[11:19]

    cv2.putText(frame , text , (10,100),cv2.FONT_HERSHEY_SIMPLEX , 1 , (255,0,255),2,cv2.LINE_AA)
    cv2.imshow('Image' , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()
