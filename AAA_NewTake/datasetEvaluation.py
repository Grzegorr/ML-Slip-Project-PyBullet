#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 21:31:03 2020

@author: greg
"""

import numpy as np
import pybullet as p
from math import *
import matplotlib.pyplot as plt
dataset_size = 130
data_location = "ProcessedDataset"

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

fail_indexes = np.zeros(dataset_size)
no_not_failed = 0
for iteration in range(dataset_size):
    #print("Processing dataset Entry: " + str(iteration))
    datasetEntry = np.load(data_location + "/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
    signals = getFaillSuccessSignals(datasetEntry)
    signals = signals.tolist()
    fail_index = signals.count(0)
    #print(fail_index)
    fail_indexes[iteration] = fail_index
    
    if fail_index == 35:
        no_not_failed = no_not_failed + 1.0
        
        
    
print("Fail Indexes:") 
print(fail_indexes)
print("Not failed percenage: " + str(100.0*no_not_failed/dataset_size))    


# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=fail_indexes, bins=36, color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.savefig("newWayOfGeneration.png")
plt.show()







 
