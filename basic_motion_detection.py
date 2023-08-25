import cv2 

cap = cv2.VideoCapture(0) 

ret , frame1 = cap.read()
ret , frame2 = cap.read()

while True:

    diff = cv2.absdiff(frame1 , frame2) 
    gray = cv2.cvtColor(diff , cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray , (5,5) , 0 )
    _ , thresh = cv2.threshold(blur , 20 , 250 , cv2.THRESH_BINARY )
    # dilate = cv2.dilate(thresh , None , iterations=3)
    contours , _ = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE )

    cv2.imshow('original frame' , frame1)


    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)

        if w*h < 1000 :
            continue 

        cv2.rectangle(frame1 , (x,y) , (x+w , y+h) , (0,255,0) , 3)

    
    # cv2.drawContours(frame1 , contours , -1 , (0,255,0) , 3)
    cv2.imshow('Video ' , frame1) 
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

    frame1 = frame2 
    ret , frame2 = cap.read() 

cap.release() 
cv2.destroyAllWindows()
