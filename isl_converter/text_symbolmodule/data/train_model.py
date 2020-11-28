import os
import sys
import csv
import cv2
import pandas as pd

import numpy as np
from sklearn import metrics
from sklearn import linear_model 
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import warnings

import pickle

def save_model (model,model_name) :
    path="./{}/model{}.pkl".format(model_name,model_name)
    pickle.dump(model,open(path,'wb'))

def generate_data (path):
    dataset=pd.read_csv(path)
    x=dataset.iloc[:, 1: ].values
    y=dataset.iloc[:,0].values
    x = preprocessing.scale(x)
    x,y = shuffle(x,y)
    return x,y

def generate_knn_classifier():
    num_neighbours = 10
    print("\nGenerating KNN model with number of neighbours = '{}'...".format(
        num_neighbours))
    classifier_model = KNeighborsClassifier(n_neighbors=num_neighbours)
    print("Done!\n")
    return classifier_model


def generate_logistic_classifier():
    print("\nGenerating Logistic-regression model...")
    classifier_model = linear_model.LogisticRegression(max_iter=10000)
    print("Done!\n")
    return classifier_model


def generate_svm_classifier():
    print("\nGenerating SVM model...")
    classifier_model = svm.SVC(kernel='poly', degree = 1)
    print("Done!\n")
    return classifier_model

def generate_random_forest_classifier() :
    print("\nGenerating Random forest classification model...")
    classifier_model = RandomForestClassifier()
    print("Done!\n")
    return classifier_model


def model_train():
    models = ['logistic', 'knn', 'svm', 'random-forest']
    for i in models :
        stat_file = open("./{}/{}_stat.txt".format(i,i), "w")
        if i == 'logistic' :
            model = generate_logistic_classifier()
        elif i == 'knn' :
            model = generate_knn_classifier()
        elif i == 'svm' :
            model = generate_svm_classifier()
        stat_file.write("model used {} classifier".format(i))
        stat_file.write("model details : \n \n {} \n".format(model))
        x_train,y_train=generate_data("train.csv")
        print("training {} model \n".format(i))
        model = model.fit(x_train,y_train)
        print("done training {} model \n".format(i))
        x_test,y_test = generate_data("test.csv")
        
        score = model.score(x_test,y_test)
        stat_file.write("{} model score \n \n {} \n".format(i,score))
        predict = model.predict(x_test)
        report = metrics.classification_report(y_test,predict)
        stat_file.write("Classification report : \n {} \n\n".format(report))
        print("{} model done ".format(i))
        save_model(model,i)
    print ("finished training")

warnings.filterwarnings('ignore')
model_train()