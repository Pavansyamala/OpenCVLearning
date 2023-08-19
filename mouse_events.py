import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
points = []

# print(events) 

def click(event , x , y , flags , param):
    # if event == cv2.EVENT_LBUTTONUP :
    #     print(x,' ',y)
    #     text = 'X: '+str(x)+' '+'Y: '+str(y)
    #     cv2.putText(image ,text, (x,y) , 
    #                 cv2.FONT_HERSHEY_SIMPLEX,
    #                 1,(255,0,255),2,cv2.LINE_AA)
    #     cv2.imshow('image' , image) 
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image , (x,y) , 3 , (255,255,255),-1)
        cv2.imshow('image',image)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(image , points[-1],points[-2],(0,255,255),4)
            cv2.imshow('image',image)

    if event == cv2.EVENT_RBUTTONDBLCLK :
        blue = image[y,x ,0]
        green = image[y,x ,1]
        red = image[y,x ,2]
        text  = str(blue) + str(green) + str(red) 
        cv2.putText(
            image , text ,
            (x,y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,255),
            2
        )
        cv2.imshow('image',image)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,' ',y)
        text = 'Kasa Pavan'
        cv2.putText(image ,text, (x,y) , 
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,(255,0,255),2,cv2.LINE_AA)
        cv2.imshow('image' , image)

    if event == cv2.EVENT_MBUTTONDBLCLK:
        text = 'Kasa syamala'
        cv2.putText(image ,text, (x,y) , 
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,(255,0,255),2,cv2.LINE_AA)
        cv2.imshow('image' , image)
    if event == cv2.EVENT_MBUTTONDOWN:
        text = 'Kasa syamala Amma '
        cv2.putText(image ,text, (x,y) , 
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,(255,0,255),2,cv2.LINE_AA)
        cv2.imshow('image' , image)

    

image = np.zeros((512,512,3),dtype=np.uint8)
cv2.imshow('image' , image)
cv2.setMouseCallback('image' , click )
cv2.waitKey(0)
cv2.destroyAllWindows()
