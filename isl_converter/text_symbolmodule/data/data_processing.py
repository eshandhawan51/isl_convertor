import os 
import sys
import cv2
import csv
import numpy as np
import image_transformation as image_processing
import matplotlib.pyplot as plt

folder = ["train","test"]
letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
for i in folder :
    output_path = open("./{}.csv".format(i),'w')
    writer = csv.writer(output_path,delimiter=',')
    print("generating {}ing data".format(i))
    for alphabets in letters:
        path =os.path.join("./dataset",i,alphabets)
        directory=r'{}'.format(path)
    
        try:
            for filename in os.listdir(directory):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    image_file=os.path.join(path, filename)
                    frame = cv2.imread(image_file)
    #                cv2.imshow("Original", frame)
                    try:
                        frame=image_processing.apply_image_transformation(frame)
                        flattened_image = frame.flatten()
                        output_image = [alphabets]+ np.array(flattened_image).tolist()
                        writer.writerow(output_image)
                    except Exception :
                        print ("failed to apply image transformation")
                        continue

                else:
                    continue
        except FileNotFoundError :
            pass
