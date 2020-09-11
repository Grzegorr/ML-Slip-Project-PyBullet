#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:29:19 2020

@author: greg
"""

import numpy as np
import pybullet as p
from math import *
from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout
import keras
from matplotlib import pyplot as plt

#location = "1_DatasetSplit"
#location = "2_xyzDiff"
#location = "3_allPoseDiff"
location = "4_UpToFail"

x = np.load(location + "/x.npy")
y = np.load(location + "/y.npy")


y = keras.utils.to_categorical(y, 2)

print("Length of x: " + str(len(x)))


x_train = x[0:50000]
y_train = y[0:50000]
x_val = x[50001:54000]
y_val = y[50001:54000]

#print(x_val)
print(len(x_train[0]))


model = Sequential()
model.add(Dense(128, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
history = model.fit(x_train, y_train,epochs=500,batch_size=32,validation_data=(x_val, y_val))
model.summary() 

#print(model.history.history)
plt.plot(model.history.history['loss'])
plt.plot(model.history.history['val_loss'])
plt.title('Model Loss on Training and Test Datasets')
plt.ylabel('CrossEntropy')
plt.xlabel('Epoch')
plt.legend(['Train-set', 'Test-set'], loc='upper left')
plt.savefig(location +"/trainingHistory.png")
plt.clf()

plt.plot(model.history.history['accuracy'])
plt.plot(model.history.history['val_accuracy'])
plt.title('Model Accuracy on Training and Test Datasets')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train-set', 'Test-set'], loc='upper left')
plt.savefig(location +"/accuracyHistory.png")


print(model.predict(x_val))
print()
print()
print()
print("Seen Example")
print(y[999])
print(model.predict(x)[999])


###Save for F score
np.save(location + "/y_predicted",model.predict(x_val))
np.save(location + "/y_GT_for_predictions",y_val)  















