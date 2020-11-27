import os 
import sys
import cv2
import numpy as np
import image_transformation as image_processing
import matplotlib.pyplot as plt

folder = ["train","test"]
letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']


for alphabets in letters:
    path =os.path.join("./dataset","train",alphabets)
    directory=r'{}'.format(path)
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_file=os.path.join(path, filename)
                frame = cv2.imread(image_file)
#                cv2.imshow("Original", frame)
                frame=image_processing.apply_image_transformation(frame)
            else:
                continue
    except FileNotFoundError :
        pass
