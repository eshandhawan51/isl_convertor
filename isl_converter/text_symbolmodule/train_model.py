import os
import sys
import csv
import cv2

import numpy as np
from sklearn import metrics
from sklearn import linear_model 
from sklearn import svm

import pickle

def save_model (model) :
    pickle.dump(model)

