#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:29:23 2020

@author: grzegorz
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, SimpleRNN, LSTM

##That was first test inputs
#x_train = [[
#        [0.54, 0.82, 0.12, 0.44],
#        [0.14, 0.56, 0.32, 0.66],
#        [0.33, 0.34, 0.52, 0.54],
#        [0.85, 0.16, 0.22, 0.33]
#        ]]
#
#x_val = [[
#        [0.54, 0.82, 0.12, 0.44],
#        [0.14, 0.56, 0.32, 0.66],
#        [0.33, 0.34, 0.52, 0.54],
#        [0.85, 0.16, 0.22, 0.33]
#        ]]
#
y_train = [[0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.88, 0.12, 0.34, 0.88, 0.12],
           [0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.88, 0.12, 0.34, 0.88, 0.12]]
y_val = y_train
#print(y_val)

NoOfTrajectories = 2
x_train = np.zeros((NoOfTrajectories,35,11))
for trajectoryNo in range(NoOfTrajectories):
    singleDatsetEntry = np.load("ProcessedDataset/TestEntry" + str(trajectoryNo) + ".npy", allow_pickle = True)
    #print(singleDatasetEntry)
    singleTaskWaypoints = singleDatsetEntry[11]
    #print(singleTaskWaypoints)
    WaypointsNoTime = singleTaskWaypoints[:,1:]
    #print(WaypointsNoTime)####flatten it to a single 1D array
    #print(len(WaypointsNoTime))
    WaypointsNoTime1D = np.zeros((35,11))
    for i in range(35):
        temp_waypoint = [WaypointsNoTime[i][0][0],WaypointsNoTime[i][0][1],WaypointsNoTime[i][0][2],WaypointsNoTime[i][1][0],WaypointsNoTime[i][1][1],WaypointsNoTime[i][1][2],WaypointsNoTime[i][1][3],WaypointsNoTime[i][2],WaypointsNoTime[i][3],WaypointsNoTime[i][4],WaypointsNoTime[i][5]]
        print(temp_waypoint)
        WaypointsNoTime1D[i] = temp_waypoint
    #print(WaypointsNoTime1D)
    x_train[trajectoryNo] =  WaypointsNoTime1D

x_train = x_train.tolist()
print(x_train)
x_val = x_train


model = Sequential()
model.add(LSTM(128,return_sequences=True,input_shape = (35,11)))
model.add(LSTM(128,return_sequences=True))
model.add(Dense(1))

model.compile(optimizer='adam',loss='mae')
history = model.fit(x_train, y_train,epochs=1000,batch_size=32,validation_data=(x_val, y_val))

print(model.predict(x_train))