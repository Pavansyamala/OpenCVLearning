import datetime
import time
import os
import sys
import cv2
print(str(datetime.datetime.now()))

# Change working directory to the images folder
os.chdir("D:\\CV(OPENCV)\\images")
images =[]
# Get a list of all files in the directory
file_list = os.listdir()

print(file_list)

# Iterate through the files and print their paths
for filename in file_list:
    file_path = os.path.join("D:\\CV(OPENCV)\\images", filename)
    images.append(cv2.imread(file_path))
    print("File:", file_path)
print(len(images))


for i in images:

    cv2.imshow('image',i)
    cv2.waitKey(0)
    # time.sleep(10)

cv2.waitKey(0)
cv2.destroyAllWindows()


