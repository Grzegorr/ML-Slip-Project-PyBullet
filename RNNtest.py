# -*- coding: utf-8 -*-
import tensorflow as tf
import random
from tensorflow import keras
from tensorflow.keras import layers

num_examples = 100000
num_classes = 50

def input_values():
    multiple_values = [map(int, '{0:050b}'.format(i)) for i in range(2 ** 20)]
    random.shuffle(multiple_values)
    final_values = []
    for value in multiple_values[:num_examples]:
        temp = []
        for number in value:
            temp.append([number])
        final_values.append(temp)
    return final_values
    
def output_values(inputs):
    final_values = []
    for value in inputs:
        output_values = [0 for _ in range(num_classes)]
        count = 0
        for i in value:
            count += i[0]
        if count < num_classes:
            output_values[count] = 1
        final_values.append(output_values)
    return final_values
    
def generate_data():
    inputs= input_values()
    return inputs, output_values(inputs)
    
    
model = keras.Sequential()
model.add(layers.Embedding(input_dim=50, output_dim=50))
model.add(layers.simpleRNN(128))
model.add(layers.Dense(256))
model.summary()

    


            
            
prediction_result = sess.run(prediction, {X: test_example})
largest_number_index = prediction_result[0].argsort()[-1:][::-1]

print("Predicted sum: ", largest_number_index, "Actual sum:", 30)
print("The predicted sequence parity is ", largest_number_index %2, " and it should be: ", 0)