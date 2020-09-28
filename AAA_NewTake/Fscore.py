#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:18:31 2020

@author: greg
"""

###CheatSheet

### TN = [>] [1,0]




import numpy as np
#location = "1_DatasetSplit"
#location = "2_xyzDiff"
#location = "3_allPoseDiff"
#location = "4_UpToFail"
#location = "1_DatasetSplitAggresive"
location = "2_xyzDiffAggresive"
#location = "3_allPoseDiffAggresive"
#location = "4_UpToFailAggresive"

try:
    y_predicted = np.load(location + "/y_predicted.npy", allow_pickle = True)
    y_GT_for_predictions = np.load(location + "/y_GT_for_predictions.npy", allow_pickle = True)
except:
    y_predicted = np.load(location + "/y_predicted.npy", allow_pickle=True)
    y_GT_for_predictions = np.load(location + "/y_GT_for_predictions.npy", allow_pickle=True)

print(y_predicted)
print(y_GT_for_predictions)

no_entries = len(y_predicted)


TP = 0
TN = 0
FP = 0
FN = 0
for i in range(no_entries):
    if y_predicted[i][0] > y_predicted[i][1]: #Negative:
        if y_GT_for_predictions[i][0] == 1: #true negative
            TN = TN + 1
        else:
            FN = FN + 1
    else:  #positive
        if y_GT_for_predictions[i][1] == 1: 
            TP = TP + 1
        else:
            FP = FP + 1

print("Results 500 epochs:  ")
print("TP: " + str(TP) + "  ")
print("FP: " + str(FP) + "  ")
print("TN: " + str(TN) + "  ")
print("FN: " + str(FN) + "  ")

F_score = (2.0*TP)/(2.0*TP + FP + FN)
print("FScore: " + str(F_score) + "  ")

acc = 1.0*(TP + TN)/(TP + TN + FP + FN)
print("Accuracy: " + str(acc) + "  ")




