#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:21:26 2020

@author: greg
"""

import numpy as np
import pybullet as p
from math import *

dataset_size = 2500
x = np.zeros((dataset_size*35, 38))
y = np.zeros(dataset_size*35)

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
    print("Simple split. Processing dataset Entry: " + str(iteration))
    datasetEntry = np.load("FinalDataset/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
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
    whole_trajectory_x = np.concatenate((tactileInfo,WaypointsNoTime1D), axis = 1)
    #print(whole_trajectory_x.shape)
    
    for event_no in range(len(whole_trajectory_x)):
        x[35*iteration + event_no,:] = whole_trajectory_x[event_no]
    #print(x)
    
    failSignals = getFaillSuccessSignals(datasetEntry)
    for event_no in range(len(whole_trajectory_x)):
        y[35*iteration + event_no] = failSignals[event_no]
    #print(y)
    
np.save("1_DatasetSplit/x",x)
np.save("1_DatasetSplit/y",y)



x = np.zeros((dataset_size*35, 38))
y = np.zeros(dataset_size*35)
for iteration in range(dataset_size):
    print("Position difference. Processing dataset Entry: " + str(iteration))
    datasetEntry = np.load("FinalDataset/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
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
        
        ###Adjustments to get the difference
        if i == 0:
            ###Subtract from starting point[0.5,0,0.5]
            temp_waypoint[0] = temp_waypoint[0] - 0.5
            temp_waypoint[2] = temp_waypoint[2] - 0.5
        else:
            ###Subtract from previous waypoint
            temp_waypoint[0] = WaypointsNoTime[i-1][0][0]
            temp_waypoint[1] = WaypointsNoTime[i-1][0][1]
            temp_waypoint[2] = WaypointsNoTime[i-1][0][2]
        
        #print(temp_waypoint)
        WaypointsNoTime1D[i] = temp_waypoint
    #print(WaypointsNoTime1D)
    
    #merge trajectoriry with tactile information just before the given waypoint starts
    whole_trajectory_x = np.concatenate((tactileInfo,WaypointsNoTime1D), axis = 1)
    #print(whole_trajectory_x.shape)
    
    for event_no in range(len(whole_trajectory_x)):
        x[35*iteration + event_no,:] = whole_trajectory_x[event_no]
    #print(x)
    
    failSignals = getFaillSuccessSignals(datasetEntry)
    for event_no in range(len(whole_trajectory_x)):
        y[35*iteration + event_no] = failSignals[event_no]
    #print(y)
    
np.save("2_xyzDiff/x",x)
np.save("2_xyzDiff/y",y)
    



x = np.zeros((dataset_size*35, 38))
y = np.zeros(dataset_size*35)
for iteration in range(dataset_size):
    print("Pose Difference. Processing dataset Entry: " + str(iteration))
    datasetEntry = np.load("FinalDataset/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
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
        
        ###Adjustments to get the difference of xyz
        if i == 0:
            ###Subtract from starting point[0.5,0,0.5]
            temp_waypoint[0] = temp_waypoint[0] - 0.5
            temp_waypoint[2] = temp_waypoint[2] - 0.5
        else:
            ###Subtract from previous waypoint
            temp_waypoint[0] = WaypointsNoTime[i-1][0][0]
            temp_waypoint[1] = WaypointsNoTime[i-1][0][1]
            temp_waypoint[2] = WaypointsNoTime[i-1][0][2]
            
        ###Adjustments to get the difference of orientation
        if i == 0:
            ###Subtract from starting point
            temp_waypoint[3] = temp_waypoint[3] - 0.7
            temp_waypoint[6] = temp_waypoint[6] - 0.7
        else:
            ###Subtract from previous waypoint
            temp_waypoint[3] = WaypointsNoTime[i-1][1][0]
            temp_waypoint[4] = WaypointsNoTime[i-1][1][1]
            temp_waypoint[5] = WaypointsNoTime[i-1][1][2]
            temp_waypoint[6] = WaypointsNoTime[i-1][1][3]
            
        
        #print(temp_waypoint)
        WaypointsNoTime1D[i] = temp_waypoint
    #print(WaypointsNoTime1D)
    
    #merge trajectoriry with tactile information just before the given waypoint starts
    whole_trajectory_x = np.concatenate((tactileInfo,WaypointsNoTime1D), axis = 1)
    #print(whole_trajectory_x.shape)
    
    for event_no in range(len(whole_trajectory_x)):
        x[35*iteration + event_no,:] = whole_trajectory_x[event_no]
    #print(x)
    
    failSignals = getFaillSuccessSignals(datasetEntry)
    for event_no in range(len(whole_trajectory_x)):
        y[35*iteration + event_no] = failSignals[event_no]
    #print(y)
    
np.save("3_allPoseDiff/x",x)
np.save("3_allPoseDiff/y",y)    




x = np.zeros((dataset_size*35, 38))
y = np.zeros(dataset_size*35)
###Next is just taking the sequences to a point where grasp fails, the rest of the sequence is dropped
###Therefore there will be no entries which are a grasp failure only because 
counter = 0
for iteration in range(dataset_size):
    print("Pose Diff, only up to first. Processing dataset Entry: " + str(iteration))
    datasetEntry = np.load("FinalDataset/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
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
        
        ###Adjustments to get the difference of xyz
        if i == 0:
            ###Subtract from starting point[0.5,0,0.5]
            temp_waypoint[0] = temp_waypoint[0] - 0.5
            temp_waypoint[2] = temp_waypoint[2] - 0.5
        else:
            ###Subtract from previous waypoint
            temp_waypoint[0] = WaypointsNoTime[i-1][0][0]
            temp_waypoint[1] = WaypointsNoTime[i-1][0][1]
            temp_waypoint[2] = WaypointsNoTime[i-1][0][2]
            
        ###Adjustments to get the difference of orientation
        if i == 0:
            ###Subtract from starting point
            temp_waypoint[3] = temp_waypoint[3] - 0.7
            temp_waypoint[6] = temp_waypoint[6] - 0.7
        else:
            ###Subtract from previous waypoint
            temp_waypoint[3] = WaypointsNoTime[i-1][1][0]
            temp_waypoint[4] = WaypointsNoTime[i-1][1][1]
            temp_waypoint[5] = WaypointsNoTime[i-1][1][2]
            temp_waypoint[6] = WaypointsNoTime[i-1][1][3]
            
        
        #print(temp_waypoint)
        WaypointsNoTime1D[i] = temp_waypoint
    #print(WaypointsNoTime1D)
    
    #merge trajectoriry with tactile information just before the given waypoint starts
    whole_trajectory_x = np.concatenate((tactileInfo,WaypointsNoTime1D), axis = 1)
    #print(whole_trajectory_x.shape)
    
    failSignals = getFaillSuccessSignals(datasetEntry)
 
    dummy = 0
    while(failSignals[dummy] == 0):
        if dummy == 34:
            break
        dummy = dummy + 1
    #print(dummy)
    failSignals = getFaillSuccessSignals(datasetEntry)
    
    
    for event_no in range(dummy+1):
        x[counter + event_no,:] = whole_trajectory_x[event_no]
    #print(x)
    
    for event_no in range(dummy+1):
        y[counter + event_no] = failSignals[event_no]
    #print(y)
    counter = counter + dummy + 1
    #print(counter)

x = x[0:counter]    
y = y[0:counter]

print(y)
np.save("4_UpToFail/x",x)
np.save("4_UpToFail/y",y)       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    