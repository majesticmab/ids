import tensorflow as tf
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import sys
import os


import_directory = "/home/mab/model_cicids_2018/"
files = os.listdir(import_directory)

counter = 0
data_array = np.empty((0, 2))

for file in files:
    if (".npy" in file):
        print('Opening File : ', file)
        data_set = np.load(import_directory + file, allow_pickle=True)
        data_array = np.vstack((data_array, data_set))