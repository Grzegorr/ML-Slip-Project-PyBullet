#!/usr/bin/env python3
# -*- coding: utf-8 -*-


validTasksCounter = 0

for x in range(150):
    datasetEntry = np.load("Tasks/PGTtest" + str(x) + ".npy", allow_pickle = True)
    if datasetEntry[]