#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

validTasksCounter = 0

for x in range(150):
    datasetEntry = np.load("Dataset/TestEntry" + str(x) + ".npy", allow_pickle = True)
    #print(datasetEntry[12])
    if datasetEntry[12] == 1:
        validTasksCounter = validTasksCounter + 1
        
print(validTasksCounter)
        