import cv2
import numpy as np

def click(event, x, y, flags, param):
    global coordinates
    if event == cv2.EVENT_LBUTTONUP:
        coordinates.add((x, y))

image = cv2.imread("D:\\DeepLearningDataCollection\\cloudy\\30.jpg") 
print(image.shape)
coordinates = set()
cv2.imshow('image', image)
cv2.setMouseCallback('image', click)
cv2.waitKey(0)
cv2.destroyAllWindows()

coordinates = list(coordinates)
print(coordinates)
woman = image[coordinates[0][1]:coordinates[1][1], coordinates[0][0]:coordinates[1][0]]
print(woman.shape)

img = np.zeros(image.shape, dtype=np.uint8)
img[coordinates[0][1]:coordinates[1][1], coordinates[0][0]:coordinates[1][0]] = woman
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
