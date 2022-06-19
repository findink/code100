# From: @lgq of CN/HITSZ/IOTS, 2022/06;
# To  : Everyone; with MIT license;
# What: python to read origin data ; 
#       input : path or dataset
#       output: train/test(formated) data
# Updater:

import os
import numpy as np
import pandas as pd
import math
import random
from datetime import datetime
import pickle
from utils import pkl_load, pad_nan_to_target
from scipy.io.arff import loadarff
from sklearn.preprocessing import StandardScaler, MinMaxScaler



def load_UCR(dataset):
    UCR_path = "datasets/UCR"
    train_path = os.path.join(UCR_path, dataset, dataset + "_TRAIN.tsv")
    test_path = os.path.join(UCR_path, dataset, dataset + "_TEST.tsv")
    train_df = pd.read_csv(train_path, sep='\t', header=None)
    test_df = pd.read_csv(test_path, sep='\t', header=None)
    train_array = np.array(train_df)
    test_array = np.array(test_df)

    train_x = train_array[:,1:]
    train_y = train_array[:,0]
    test_x  = test_array[:,1:]
    test_y  = test_array[:,0]




load_UCR(ss)