#HAND GESTURE RECOGNIZATION USING OPENCV
import numpy as np
import cv2
import math
from isl_converter.video_processing import image_transformation as image_processing
import pickle

      
def image_modification(frame):

        l = len(frame) - 100
        crop_image=frame[100:l,100:l]
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
        #cv2.imshow("Threshold",thres)
        thres=image_processing.apply_image_transformation(thres,1)
        cv2.imshow("test",thres)
        return thres

