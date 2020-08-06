#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:29:23 2020

@author: grzegorz
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, SimpleRNN, LSTM

def getFaillSuccessSignals(datasetEntry):
    signals = np.zeros(35)
    graspFailFlags = datasetEntry[7]
    for waypoint in range(35):
        #print(waypoint)
        startIndex = 6500 + waypoint * 500
        endIndex = startIndex + 500
        batchOfSignals = graspFailFlags[startIndex:endIndex]
        #print(len(batchOfSignals))
        #print(np.count_nonzero(batchOfSignals == 1))
        no_fails = np.count_nonzero(batchOfSignals == 1)
        if no_fails > 0:
            signals[waypoint] = 1
        else:
            signals[waypoint] = 0
    #print(signals)
    return signals

def physicalModelAcceleration(datasetEntry):
    final_accelerations =  np.zeros((35,3))
    accelerations = datasetEntry[13]
    #print(len(accelerations))
    for waypoint in range(35):
        #print(waypoint)
        Index = 6501 + waypoint * 500
        final_accelerations[waypoint][:] = accelerations[Index]
    #print(final_accelerations)
    return final_accelerations

def getThresholds(accelerations):
    thresholds = np.zeros(35)
    calibration = np.load("Calibration/Calibration_cylinder.npy", allow_pickle = True)
    for waypoint in range(35):
        theta = int(accelerations[waypoint][0])
        phi = int(accelerations[waypoint][1])
        threshold = calibration[theta][phi]
        thresholds[waypoint] = threshold
    #print(thresholds)
    return thresholds

def groundTruth(thresholds,accelerations,failSignals):
    GT = np.zeros(35)
    for waypoint in range(35):
        #gt = threshold - acceleration +/- 20
        gt = thresholds[waypoint] - accelerations[waypoint][2]
        if failSignals[waypoint] == 1:
            gt = gt + 20
        else:
            gt = gt - 20
        gt = gt/700.0#Normalization
        GT[waypoint] = gt
    return GT
        
        
        
        
        

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
#y_train = [[0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.88, 0.12, 0.34, 0.88, 0.12],
#           [0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.23, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12, 0.34, 0.88, 0.12,0.88, 0.12, 0.34, 0.88, 0.12]]
#y_val = y_train
#print(y_val)

NoOfTrajectories = 20
x = np.zeros((NoOfTrajectories,35,11))
y = np.zeros((NoOfTrajectories,35))
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
        #print(temp_waypoint)
        WaypointsNoTime1D[i] = temp_waypoint
    #print(WaypointsNoTime1D)
    x[trajectoryNo] =  WaypointsNoTime1D
    
    #Get on/off signals for grasp succes or fail 1 - fail, 0 is success
    failSignals = getFaillSuccessSignals(singleDatsetEntry)
    #get accelerations from physical model
    accelerations = physicalModelAcceleration(singleDatsetEntry)
    #getting finl thresholds
    thresholds = getThresholds(accelerations)
    #finaly translate it into ground truth for residual for learning
    ground_truth = groundTruth(thresholds,accelerations,failSignals)
    y[trajectoryNo] = ground_truth

x = x.tolist()
y = y.tolist()



model = Sequential()
model.add(LSTM(64,return_sequences=True,input_shape = (35,11)))
#model.add(LSTM(128,return_sequences=True))
#model.add(LSTM(64,return_sequences=True))
model.add(Dense(1))

model.compile(optimizer='adam',loss='mse')
history = model.fit(x, y,epochs=2000,batch_size=32,validation_data=(x, y))

print(y)
print(model.predict(x))