# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:42:29 2020

@author: computing
"""
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, SimpleRNN, LSTM
model = Sequential()


def OnOffPredict(modelAccelerations, residuals, thresholds):
    predictions = np.zeros(35)
    for waypoint in range(35):
        predictedForce = modelAccelerations[waypoint]/700.0 + residuals[waypoint]
        #print(predictedForce)
        if predictedForce > thresholds[waypoint]/700.0:
            predictions[waypoint] = 1
        else:
            predictions[waypoint] = 0
    return predictions 

model = keras.models.load_model("TrainedNetworks/LSTM_64_128_64_1000examples_2000epochs_NoDropout.h5")

x = np.load("Learning_Res/x.npy")
y = np.load("Learning_Res/y.npy")
Thresholds = np.load("Learning_Res/Thresholds.npy")
Accelerations = np.load("Learning_Res/Accelerations.npy")
ONOFFGroundTruth = np.load("Learning_Res/ONOFFGroundTruth.npy")


print()
print()
print()
print("Seen Example")
print("Residual Ground Truth:")
print(y[999])
residuals = model.predict(x)[999]
print("Residuals Predicted")
print(model.predict(x)[999])

graspPredictions = OnOffPredict(Accelerations[999],residuals,Thresholds[999])
print("Grasp Predictions from the system")
print(graspPredictions)
print("Grasp - Ground Truth")
print(ONOFFGroundTruth[999])






print()
print()
print()
print("Unseen Example")
print(y[1000])
residuals = model.predict(x)[1000]
print(model.predict(x)[1000])

graspPredictions = OnOffPredict(Accelerations[1000],residuals,Thresholds[1000])
print("Grasp Predictions from the system")
print(graspPredictions)
print("Grasp - Ground Truth")
print(ONOFFGroundTruth[1000])

print()
print()
print()
print("Another Unseen Example")
print(y[1001])
residuals = model.predict(x)[1001]
print(model.predict(x)[1001])

graspPredictions = OnOffPredict(Accelerations[1001],residuals,Thresholds[1001])
print("Grasp Predictions from the system")
print(graspPredictions)
print("Grasp - Ground Truth")
print(ONOFFGroundTruth[1000])










