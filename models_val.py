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
   
   
def multiplePredict(starIndex,endIndex,model):
    print()


model = keras.models.load_model("TrainedNetworks/LSTM_256_256_128_900examples_2000epochs_NoDropout_LastLayerLSTM.h5")

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
print(y[899])
residuals = model.predict(x)[899]
print("Residuals Predicted")
print(model.predict(x)[899])

graspPredictions = OnOffPredict(Accelerations[899],residuals,Thresholds[899])
print("Grasp Predictions from the system")
print(graspPredictions)
print("Grasp - Ground Truth")
print(ONOFFGroundTruth[899])


print()
print()
print()
print("Unseen Example")
print(y[900])
residuals = model.predict(x)[900]
print(model.predict(x)[900])

graspPredictions = OnOffPredict(Accelerations[900],residuals,Thresholds[900])
print("Grasp Predictions from the system")
print(graspPredictions)
print("Grasp - Ground Truth")
print(ONOFFGroundTruth[900])

print()
print()
print()
print("Another Unseen Example")
print(y[901])
residuals = model.predict(x)[901]
print(model.predict(x)[901])

graspPredictions = OnOffPredict(Accelerations[901],residuals,Thresholds[901])
print("Grasp Predictions from the system")
print(graspPredictions)
print("Grasp - Ground Truth")
print(ONOFFGroundTruth[901])










