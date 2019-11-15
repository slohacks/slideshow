import cv2
import numpy as np 
import os, time




# we define the location of the folder
my_location = "images/" 

# we loop through the files inside the folder
for file in os.listdir(my_location):

# we read a file    
    img = cv2.imread(my_location + '/' + file)
    print(file)

    cv2.imshow('mems',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
cv2.destroyAllWindows()
