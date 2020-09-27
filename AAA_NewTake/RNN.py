#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:38:36 2020

@author: greg
"""

import numpy as np
import pybullet as p
from math import *
from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout, LSTM, RNN
import keras
from matplotlib import pyplot as plt
import tensorflow as tf

import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

location = "7_RNN"
#location = "8_RNNT1"
#location = "9_RNNT2"
#location = "10_RNNT3"
#location = "11_RNNT4"
#location = "12_RNNT5"


x = np.load(location + "/x.npy")
y = np.load(location + "/y.npy")


y = keras.utils.to_categorical(y, 2)

print("Length of x: " + str(len(x)))

length = int(len(x))
boundry = int(0.9 * len(x))
x_train = x[0:boundry]
y_train = y[0:boundry]
x_val = x[boundry + 1:length]
y_val = y[boundry + 1:length]




#print(x_val)
#print(len(x_train[0]))


model = Sequential()
model.add(LSTM(128,return_sequences=True, activation='relu',input_shape = (35,38)))
model.add(LSTM(256, activation='relu',return_sequences=True))
model.add(LSTM(128, activation='relu',return_sequences=True))
model.add(Dense(2,activation = 'softmax'))
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
history = model.fit(x_train, y_train,epochs=2000,batch_size=32,validation_data=(x_val, y_val))
model.summary()
print("Training Finished.")



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


print("Example Prediction")
print("GT: " + str(y[999]))
print("Prediction" + str(model.predict(x)[999]))





































