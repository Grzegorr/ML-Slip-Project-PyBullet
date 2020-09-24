#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:10:10 2020

@author: greg
"""

import numpy as np

dataset_size = 3200
x = np.zeros((dataset_size, 35, 38))
y = np.zeros((dataset_size, 35))


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



for iteration in range(dataset_size):
    print("Processing dataset Entry: " + str(iteration))
    datasetEntry = np.load("FinalDataset/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
    tactileInfo = prepareTactileData(datasetEntry)
    tactileInfo = prepareTactileData(datasetEntry)
    #print(tactileInfo)
    
    singleTaskWaypoints = datasetEntry[11]
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
    x_temp = np.concatenate((tactileInfo,WaypointsNoTime1D), axis = 1)
    #print(whole_trajectory_x.shape)
    
    y_temp = getFaillSuccessSignals(datasetEntry)
    
    
    x[iteration,:,:] = x_temp
    y[iteration,:] = y_temp



np.save("7_RNN/x",x)
np.save("7_RNN/y",y)
    
###TimeShifts######

for i in range(len(y)):
    x[i,0:34,0:27] = x[i,1:35,0:27]
    x[i, 34, 0:27] = np.zeros(27)
np.save("8_RNNT1/x",x)
np.save("8_RNNT1/y",y)

for i in range(len(y)):
    x[i, 0:34, 0:27] = x[i, 1:35, 0:27]
    x[i, 34, 0:27] = np.zeros(27)
np.save("9_RNNT2/x",x)
np.save("9_RNNT2/y",y)


for i in range(len(y)):
    x[i, 0:34, 0:27] = x[i, 1:35, 0:27]
    x[i, 34, 0:27] = np.zeros(27)
np.save("10_RNNT3/x",x)
np.save("10_RNNT3/y",y)


for i in range(len(y)):
    x[i, 0:34, 0:27] = x[i, 1:35, 0:27]
    x[i, 34, 0:27] = np.zeros(27)
np.save("11_RNNT4/x",x)
np.save("11_RNNT4/y",y)


for i in range(len(y)):
    x[i, 0:34, 0:27] = x[i, 1:35, 0:27]
    x[i, 34, 0:27] = np.zeros(27)
np.save("12_RNNT5/x",x)
np.save("12_RNNT5/y",y)


for i in range(len(y)):
    x[i, 0:34, 0:27] = x[i, 1:35, 0:27]
    x[i, 34, 0:27] = np.zeros(27)
np.save("13_RNNT6/x",x)
np.save("13_RNNT6/y",y)


































