import pickle
import numpy as np
import os
                
def predict (frame):
    path =path=os.getcwd()+"/isl_converter/text_symbolmodule/data/knn/modelknn.pkl"
    model = pickle.load(open(path,"rb"))
    flattened_image = frame.flatten()
    output_image = np.array(flattened_image)
    letter = model.predict([output_image])
    return letter

