import cv2 

img = cv2.imread("D:\\_Underneath a p 1.png",1)

## Drawing Line 
img = cv2.line(img , (0,0),(100,100) , (0,0,255) , 3 )

'''
(0,0) -> Point1 from where the line starts 
(100,100) -> Pom=int2 where the line ends 
(255,0,0) --> Color Format in BGR for Blue -> (255,0,0) , Green -> (0,255,0) , Red -> (0,0,255)
3 -> Thickness of the line

if you want to pick any other color go to this website and place the control panel wherever you want and then it dispals the tuple in rgb format convert into bgr just reverse it 

Link :  https://www.google.com/search?q=rgb+color+picker&rlz=1C1RXQR_enIN988IN988&oq=rgb+color+picker&aqs=chrome..69i57j0i512l9.4399j0j7&sourceid=chrome&ie=UTF-8
'''
# For drawing arrowed line
img = cv2.arrowedLine(img , (0,0),(100,100) , (0,0,255) , 3 )

# For drawing Rectangle 
img = cv2.rectangle(img,(105,105),(205,205),(0,255,0),-1)
# In case of thickness if you will give -1 in rectangle case it will fills the rectangle completely

## Drawing Circle

img = cv2.circle(img , (305,305),100,(255,0,0),4)
'''
Argument 1 -> image on which we need to draw the circle 
Argument 2 -> Centre of the circle
Argument 3 -> Radius of the circle
Argument 5 -> Color  of the Circle
Argument 5 -> Thickness of  Circle
'''

## Adding Text to the Image 
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img , 'Relation Between Mother and Son' , (10,500) , font , 1 , (255,255,255) , 4 , cv2.LINE_AA)

'''
Argument 1 -> Imge on which we need to write Text 
Argument 2 -> Text Which you Need to Write 
Argument 3 -> Starting Cordinates of the Text
Argument 4 -> Type of the Font You want (there are lot of Fonts available in the CV2 library type CV2.FONT_ then lot of options appear then select any one from them)
Argument 5 -> Font Size
Argument 6 -> Color of the Text 
Argument 7 -> Thickness 
Argument 8 -> Line TYpe (Type cv2.LINE_ (lot of options available))
'''


cv2.imshow('Mother',img )

cv2.waitKey(10000)
cv2.destroyAllWindows()
