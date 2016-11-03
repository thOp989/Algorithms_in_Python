# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:29:06 2016

@author: Tim
"""

import pandas as pd
import numpy as np

import csv
import random
def loadDataSet(filename):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter = ';')
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(len(dataset[x])):
                if (x != 0): #The first column will have descriptions for each column. 
                    dataset[x][y] = float(dataset[x][y])
        trainingSet = dataset
        return trainingSet


# Data into vectors
def dataVectors(dataset):
    X = np.array(dataset[1][0:11])
    Y = np.array(dataset[1][11])
    
    for x in range(len(dataset)-2):
        X = np.append(X,dataset[x+2][0:11])
        Y = np.append(Y, dataset[x+2][11], axis = 0)
    return X, Y
    
# Find result vector dependent variable Y and indendent variable X.
# Use least-square estimations to find coefficient vector. 

filename = 'C:/Users/Tim/Documents/winequality-red.csv'
dataset = loadDataSet(filename)
#X, Y = dataVectors(dataset)
X = np.array(dataset[1][0:11])

X = np.append(X,[dataset[2][0:11]], axis = 0)

print (X)
