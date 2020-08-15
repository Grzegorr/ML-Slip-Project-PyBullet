# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:42:29 2020

@author: computing
"""
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, SimpleRNN, LSTM
from matplotlib import pyplot as plt

models = ["TrainedNetworks/LSTM_32_64_900examples_1000epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_32_64_900examples_1600epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_32_64_900examples_2000epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_256_256_128_900examples_1000epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_256_256_128_900examples_1600epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_256_256_128_900examples_2000epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_64_128_64_900examples_1000epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_64_128_64_900examples_1600epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_64_128_64_900examples_2000epochs_NoDropout_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_256_256_128_900examples_400epochs_Dropout_50_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_256_256_128_900examples_1200epochs_Dropout_50_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_256_256_128_900examples_2000epochs_Dropout_50_LastLayerLSTM.h5",
          "TrainedNetworks/LSTM_256_256_128_900examples_400epochs_Dropout_50_LastLayerLSTM.h5"]
          
models_taskOnly = ["TrainedNetworks/LSTM_TaskOnly_128_64_900examples_200epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_400epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_600epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_800epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_1000epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_1200epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_1400epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_1600epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_1800epochs_NoDropout_LastLayerLSTM.h5",
                    "TrainedNetworks/LSTM_TaskOnly_128_64_900examples_2000epochs_NoDropout_LastLayerLSTM.h5"
                   ]
                  
models_smallNetwork = [
                        "TrainedNetworks/LSTM_32_64_900examples_200epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_32_64_900examples_400epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_32_64_900examples_600epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_32_64_900examples_1000epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_32_64_900examples_1400epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_32_64_900examples_2000epochs_NoDropout_LastLayerLSTM.h5"
                        ]
                        
models_mediumNetwork = [
                        "TrainedNetworks/LSTM_64_128_64_900examples_200epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_64_128_64_900examples_400epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_64_128_64_900examples_600epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_64_128_64_900examples_1000epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_64_128_64_900examples_1400epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_64_128_64_900examples_2000epochs_NoDropout_LastLayerLSTM.h5"
                        ]
                        
models_largeNetwork = [
                        "TrainedNetworks/LSTM_256_256_128_900examples_200epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_256_256_128_900examples_400epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_256_256_128_900examples_600epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_256_256_128_900examples_1000epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_256_256_128_900examples_1400epochs_NoDropout_LastLayerLSTM.h5",
                        "TrainedNetworks/LSTM_256_256_128_900examples_2000epochs_NoDropout_LastLayerLSTM.h5"
                        ]
                        
historyToPlot = [
                    "TrainedNetworks/LSTM_256_256_128_900examples_2000epochs_NoDropout_LastLayerLSTM.h5"
                ]                        
                        
                        
def plotHistoricalLoss(model,model_name):
    model.summary()
    print(model.history)
    plt.cla()
    plt.plot(model.history['loss'])
    plt.plot(model.history['val_loss'])
    plt.title('Model Loss on Training and Test Datasets')
    plt.ylabel('Mean Squared Error')
    plt.xlabel('Epoch')
    plt.ylim((0,1))
    plt.legend(['Train-set', 'Test-set'], loc='upper left')
    plt.savefig("HistoryPlots/" + str(model_name) + ".png")                       

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
   
   
def multiplePredict(startIndex,endIndex,model,model_name,x,y,Accelerations,ONOFFGroundTruth,Thresholds):
    error = 0
    predictions = model.predict(x[startIndex:endIndex])
    #print(predictions)
    groundTruthResidual = y[startIndex:endIndex]
    for prediction in range(len(predictions)):
        for waypoint in range(35):        
            error = error + abs(predictions[prediction][waypoint] - groundTruthResidual[prediction][waypoint]) 
    mean_absolute_error = error/(35*(endIndex-startIndex))
    print()
    print()
    print("Model Name: " + str(model_name))
    print("Prediction of the acceleration residual mean average error(Unseen Data): " + str(mean_absolute_error))
    
    
    
    ONOFFErrors = 0
    for i in range(startIndex,endIndex):
        #print(i)
        OnOffpreds = OnOffPredict(Accelerations[i],predictions[i-startIndex],Thresholds[i])
        GT = ONOFFGroundTruth[i]
        for pred in range(35):
            if OnOffpreds[pred] != GT[pred]:
                ONOFFErrors = ONOFFErrors + 1
    ONOFFpercent = 100.0*ONOFFErrors/35/(endIndex-startIndex)
    print("Percentage of OnOFF predicions right(Unseen Data): " + str(100 - ONOFFpercent) + "%.")
    
        
    error = 0
    predictions = model.predict(x[0:startIndex])
    #print(predictions)
    groundTruthResidual = y[0:startIndex]
    for prediction in range(len(predictions)):
        for waypoint in range(35):        
            error = error + abs(predictions[prediction][waypoint] - groundTruthResidual[prediction][waypoint]) 
    mean_absolute_error = error/(35*(startIndex))
    print("Prediction of the acceleration residual mean average error(Training Data): " + str(mean_absolute_error))
    
    
    ONOFFErrors = 0
    for i in range(startIndex):
        OnOffpreds = OnOffPredict(Accelerations[i],predictions[i],Thresholds[i])
        GT = ONOFFGroundTruth[i]
        for pred in range(35):
            if OnOffpreds[pred] != GT[pred]:
                ONOFFErrors = ONOFFErrors + 1
    ONOFFpercent = 100.0*ONOFFErrors/35/(startIndex)
    print("Percentage of OnOFF predicions right(Training Data): " + str(100 - ONOFFpercent) + "%.")
    
    
    
    

def fullModelAssessment(model_name,startIndex,endIndex,x,y,Accelerations,ONOFFGroundTruth,Thresholds):
    #print(model_name)
    model = keras.models.load_model(model_name)
    multiplePredict(startIndex,endIndex,model,model_name,x,y,Accelerations,ONOFFGroundTruth,Thresholds)
    


x = np.load("Learning_Res/x.npy")
y = np.load("Learning_Res/y.npy")
Thresholds = np.load("Learning_Res/Thresholds.npy")
Accelerations = np.load("Learning_Res/Accelerations.npy")
ONOFFGroundTruth = np.load("Learning_Res/ONOFFGroundTruth.npy")

#for model_name in models:
#for model_name in models_taskOnly:
#for model_name in models_smallNetwork:
#for model_name in models_mediumNetwork:
#for model_name in models_largeNetwork:
#    fullModelAssessment(model_name,900,1000,x,y,Accelerations,ONOFFGroundTruth,Thresholds)





for model_name in historyToPlot:
    model = keras.models.load_model(model_name)
    plotHistoricalLoss(model,model_name)



#model = keras.models.load_model(model_name)
#multiplePredict(900,1000,model,x,y,Accelerations,ONOFFGroundTruth,Thresholds)
#print()
#print()
#print()
#print("Seen Example")
#print("Residual Ground Truth:")
#print(y[899])
#residuals = model.predict(x)[899]
#print("Residuals Predicted")
#print(model.predict(x)[899])
#
#graspPredictions = OnOffPredict(Accelerations[899],residuals,Thresholds[899])
#print("Grasp Predictions from the system")
#print(graspPredictions)
#print("Grasp - Ground Truth")
#print(ONOFFGroundTruth[899])
#
#
#print()
#print()
#print()
#print("Unseen Example")
#print(y[900])
#residuals = model.predict(x)[900]
#print(model.predict(x)[900])
#
#graspPredictions = OnOffPredict(Accelerations[900],residuals,Thresholds[900])
#print("Grasp Predictions from the system")
#print(graspPredictions)
#print("Grasp - Ground Truth")
#print(ONOFFGroundTruth[900])
#
#print()
#print()
#print()
#print("Another Unseen Example")
#print(y[901])
#residuals = model.predict(x)[901]
#print(model.predict(x)[901])
#
#graspPredictions = OnOffPredict(Accelerations[901],residuals,Thresholds[901])
#print("Grasp Predictions from the system")
#print(graspPredictions)
#print("Grasp - Ground Truth")
#print(ONOFFGroundTruth[901])










