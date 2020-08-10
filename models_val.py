# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:42:29 2020

@author: computing
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, SimpleRNN, LSTM
model = Sequential()
model.load("TrainedNetworks/LSTM_64_128_64_1000examples_2000epochs_NoDropout.h5")

