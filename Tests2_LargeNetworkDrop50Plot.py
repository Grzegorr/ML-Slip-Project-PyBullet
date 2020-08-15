#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:29:23 2020

@author: grzegorz
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, SimpleRNN, LSTM, Dropout
from matplotlib import pyplot as plt

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
    print(signals)
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
    #print(len(calibration))
    for waypoint in range(35):
        theta = int(accelerations[waypoint][0]) - 1
        if theta < 0:
            theta = theta + 36
        phi = int(accelerations[waypoint][1])
        #print(phi)
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

def prepareTactileData(datasetEntry):
    tactileInformation = np.zeros((35,27))
    #print("New Data Entry:")
    #print(dataEntry[0])
    proximal1_1000 = datasetEntry[0]
    proximal2_1000 = datasetEntry[1]
    proximal3_1000 = datasetEntry[2]
    distal1_1000 = datasetEntry[3]
    distal2_1000 = datasetEntry[4]
    distal3_1000 = datasetEntry[5]
    #print(len(proximal1_1000))
    #indexes of tactile sensor reading just before the the start of next waypoint
    indices = [270, 291, 312, 333, 354, 375, 395, 416, 437, 458, 479, 500, 520, 541, 562, 583, 604, 625, 645, 666, 687, 708, 729, 750, 770, 791, 812, 833, 854, 875, 895, 916, 937, 958, 979]
    #print(len(indices))
    for waypoint in range(35):
        i = indices[waypoint] # timestep of tactile observation
        #print(proximal1_1000[i][:])
        tactileInformation[waypoint][:] = np.concatenate((proximal1_1000[i][:], proximal2_1000[i][:], proximal3_1000[i][:], distal1_1000[i][:], distal2_1000[i][:], distal3_1000[i][:]))
        #print(tactileInformation[waypoint])
    return tactileInformation
    
    
def OnOffPredict(modelAccelerations, residuals, thresholds):
    predictions = np.zeros(35)
    for waypoint in range(35):
        predictedForce = modelAccelerations[waypoint]/700.0 + residuals[waypoint]
        print(predictedForce)
        if predictedForce > thresholds[waypoint]/700.0:
            predictions[waypoint] = 1
        else:
            predictions[waypoint] = 0
    return predictions 
        
    
    
    

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

NoOfTrajectories = 1000
x = np.zeros((NoOfTrajectories,35,38))
y = np.zeros((NoOfTrajectories,35))
Thresholds = np.zeros((NoOfTrajectories,35))
Accelerations = np.zeros((NoOfTrajectories,35))
ONOFFGroundTruth = np.zeros((NoOfTrajectories,35))
for trajectoryNo in range(NoOfTrajectories):
    print(trajectoryNo)
    singleDatasetEntry = np.load("ProcessedDataset/TestEntry" + str(trajectoryNo) + ".npy", allow_pickle = True)
    #print(singleDatasetEntry)
    #prepare tactile information
    tactileInfo = prepareTactileData(singleDatasetEntry)
    
    
    
    singleTaskWaypoints = singleDatasetEntry[11]
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
    
    
    
    #merge trajectoriry with tactile information just before the given waypoint starts
    x[trajectoryNo] = np.concatenate((tactileInfo,WaypointsNoTime1D), axis = 1)
    
        
    
    #Get on/off signals for grasp succes or fail 1 - fail, 0 is success
    failSignals = getFaillSuccessSignals(singleDatasetEntry)
    ONOFFGroundTruth[trajectoryNo,:] = failSignals[:]
    #get accelerations from physical model
    accelerations = physicalModelAcceleration(singleDatasetEntry)
    Accelerations[trajectoryNo,:] = accelerations[:,2]
    #getting finl thresholds
    thresholds = getThresholds(accelerations)
    Thresholds[trajectoryNo,:] = thresholds[:]
    #finaly translate it into ground truth for residual for learning
    ground_truth = groundTruth(thresholds,accelerations,failSignals)
    y[trajectoryNo] = ground_truth
    
np.save("Learning_Res/x",x)
np.save("Learning_Res/y",y)
np.save("Learning_Res/Thresholds",Thresholds)
np.save("Learning_Res/Accelerations",Accelerations)
np.save("Learning_Res/ONOFFGroundTruth",ONOFFGroundTruth)

x = x.tolist()
y = y.tolist()
x_train = x[0:900]
y_train = y[0:900]
x_val = x[900:1000]
y_val = y[900:1000]
print(len(x_train))



model = Sequential()
model.add(LSTM(256,return_sequences=True,input_shape = (35,38)))
Dropout(0.5)
model.add(LSTM(256,return_sequences=True))
Dropout(0.5)
model.add(LSTM(128,return_sequences=True))
Dropout(0.5)
model.add(LSTM(1,return_sequences=True))

model.compile(optimizer='adam',loss='mse')





history = model.fit(x_train, y_train,epochs=2000,batch_size=32,validation_data=(x_val, y_val))

print(model.history)
plt.plot(model.history.history['loss'])
plt.plot(model.history.history['val_loss'])
plt.title('Model Loss on Training and Test Datasets')
plt.ylabel('Mean Squared Error')
plt.xlabel('Epoch')
plt.ylim((0,0.05))
plt.legend(['Train-set', 'Test-set'], loc='upper left')
plt.savefig("HistoryPlots/LargeNwtwork2000Drop50.png")






print()
print()
print()
print("Seen Example")
print(y[999])
residuals = model.predict(x)[999]
print(model.predict(x)[999])

graspPredictions = OnOffPredict(Accelerations[999],residuals,Thresholds[999])
print("Grasp Predictions from the system")
print(graspPredictions)
print("Grasp - Ground Truth")
print(ONOFFGroundTruth[999])






#print()
#print()
#print()
#print("Unseen Example")
#print(y[1000])
#residuals = model.predict(x)[1000]
#print(model.predict(x)[1000])
#
#graspPredictions = OnOffPredict(Accelerations[1000],residuals,Thresholds[1000])
#print("Grasp Predictions from the system")
#print(graspPredictions)
#print("Grasp - Ground Truth")
#print(ONOFFGroundTruth[1000])












