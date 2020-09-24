#HAND GESTURE RECOGNIZATION USING OPENCV
import numpy as np
import cv2
import math

capture=cv2.VideoCapture(0)
while capture.isOpened():
    check,frame=capture.read()
    
    cv2.rectangle(frame,(100,100),(300,300), (0,255,0),0)
    crop_image=frame[100:300,100:300]
    
    blur=cv2.GaussianBlur(crop_image,(3,3),0)
    
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    
    #create a binary image where white will be skin colors and rest is black
    mask2=cv2.inRange(hsv,np.array([2,0,0]),np.array([20,255,255]))
    
    #kernal for morphological transformation
    kernel=np.ones((5,5), np.uint8)
    
    #apply morphological transformarions to filter out the background noise
    dilated=cv2.dilate(mask2,kernel,iterations=0)
    erosion=cv2.erode(dilated,kernel,iterations=0)
    
    filtered=cv2.GaussianBlur(erosion,(3,3),0)
    check,thres=cv2.threshold(filtered, 200, 225, cv2.THRESH_BINARY)
    
    cv2.imshow("Threshold",thres)
    
   
    cv2.imshow("Gesture",frame)
        #close the camera if 'q' is pressed
    if cv2.waitKey(1)==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
