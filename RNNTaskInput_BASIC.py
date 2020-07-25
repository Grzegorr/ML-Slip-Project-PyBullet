#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:29:23 2020

@author: grzegorz
"""

from keras.models import Sequential
from keras.layers import Flatten, Dense, SimpleRNN, LSTM

x_train = [[
        [0.54, 0.82, 0.12, 0.44],
        [0.14, 0.56, 0.32, 0.66],
        [0.33, 0.34, 0.52, 0.54],
        [0.85, 0.16, 0.22, 0.33]
        ]]

x_val = [[
        [0.54, 0.82, 0.12, 0.44],
        [0.14, 0.56, 0.32, 0.66],
        [0.33, 0.34, 0.52, 0.54],
        [0.85, 0.16, 0.22, 0.33]
        ]]

y_train = [[0.23, 0.34, 0.88, 0.12]]
y_val = [[0.23, 0.34, 0.88, 0.12]]


model = Sequential()
model.add(LSTM(128,return_sequences=True,input_shape = (4,4)))
model.add(LSTM(128,return_sequences=True))
model.add(Dense(1))

model.compile(optimizer='adam',loss='mae')
history = model.fit(x_train, y_train,epochs=200,batch_size=32,validation_data=(x_val, y_val))

print(model.predict(x_train))