# From: @lgq of CN/HITSZ/IOTS, 2022/06;
# To  : Everyone; with MIT license;
# What: python to read origin data ; 
#       input : path or dataset
#       output: train/test(formated) data
# Updater:

from cProfile import label
import os
import numpy as np
import pandas as pd
import math
import random

import data_plot


def load_UCR(dataset):
    UCR_path = "../datasets/UCR"
    train_path = os.path.join(UCR_path, dataset, dataset + "_TRAIN.tsv")
    test_path = os.path.join(UCR_path, dataset, dataset + "_TEST.tsv")
    train_df = pd.read_csv(train_path, sep='\t', header=None)
    test_df = pd.read_csv(test_path, sep='\t', header=None)
    train_array = np.array(train_df)
    test_array = np.array(test_df)

    # From labels to class_number:{0,1,2,...,C-1}
    labels = np.unique(train_array[:,0])
    labels_dict ={}
    for i,label in enumerate(labels):
        labels_dict[label] = i
    
    
    train_x = train_array[:,1:]
    train_y =np.vectorize(labels_dict.get)(train_array[:,0])  # use np.vectorize(func)(arr)  to process each element in arr
    test_x  = test_array[:,1:]
    test_y  =np.vectorize(labels_dict.get)(test_array[:,0]) 

    # for datasets not normalized
    if dataset  in [
        'AllGestureWiimoteX',
        'AllGestureWiimoteY',
        'AllGestureWiimoteZ',
        'BME',
        'Chinatown',
        'Crop',
        'EOGHorizontalSignal',
        'EOGVerticalSignal',
        'Fungi',
        'GestureMidAirD1',
        'GestureMidAirD2',
        'GestureMidAirD3',
        'GesturePebbleZ1',
        'GesturePebbleZ2',
        'GunPointAgeSpan',
        'GunPointMaleVersusFemale',
        'GunPointOldVersusYoung',
        'HouseTwenty',
        'InsectEPGRegularTrain',
        'InsectEPGSmallTrain',
        'MelbournePedestrian',
        'PickupGestureWiimoteZ',
        'PigAirwayPressure',
        'PigArtPressure',
        'PigCVP',
        'PLAID',
        'PowerCons',
        'Rock',
        'SemgHandGenderCh2',
        'SemgHandMovementCh2',
        'SemgHandSubjectCh2',
        'ShakeGestureWiimoteZ',
        'SmoothSubspace',
        'UMD'
    ]:
        mean = np.nanmean(train_x)
        std = np.nanstd(train_x)
        train_x = (train_x - mean)/std
        test_x = (test_x - mean)/std    # test data ,unkown&rare: so use train_data's mean & std
     
    return train_x[..., np.newaxis], train_y, test_x[..., np.newaxis], test_y  # add 


x1,x2,x3,x4 = load_UCR("ECG200")
print(x1)

data_plot.plot_y(x1[3])
