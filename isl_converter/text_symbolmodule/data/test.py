import joblib 
import image_transformation
import cv2
import numpy as np

model = joblib.load("./svm/model-serialized-svm.pkl")
image_file='/home/nolife/projects/isl_convertor/isl_converter/text_symbolmodule/data/dataset/test/x/560.jpg'
frame = cv2.imread(image_file,1)
frame = image_transformation.apply_image_transformation(frame)
flattened_image = frame.flatten()
output_image = np.array(flattened_image)
print (model.predict([output_image]))