#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pybullet as p
from math import *

np.set_printoptions(precision = 8, suppress = True)

def RPYrotation(vec,RPY):
    Rx = [
        [1,0,0],
        [0, cos(RPY[0]) , -sin(RPY[0])],
        [0, sin(RPY[0]), cos(RPY[0])]
        ]
    Ry = [
        [cos(RPY[1]), 0, sin(RPY[1])],
        [0,1,0],
        [-sin(RPY[1]), 0, cos(RPY[1])]
        ]
    Rz = [
        [cos(RPY[2]), -sin(RPY[2]), 0],
        [sin(RPY[2]), cos(RPY[2]), 0],
        [0, 0, 1]
        ]
    vector = np.transpose(vec)
    result = Rx @ vector
    result = Ry @ result
    result = Rz @ result
    print(result)
    
def inverseRPYrotation(vec,RPY):
    Rx = [
        [1,0,0],
        [0, cos(-RPY[0]) , -sin(-RPY[0])],
        [0, sin(-RPY[0]), cos(-RPY[0])]
        ]
    Ry = [
        [cos(-RPY[1]), 0, sin(-RPY[1])],
        [0,1,0],
        [-sin(-RPY[1]), 0, cos(-RPY[1])]
        ]
    Rz = [
        [cos(-RPY[2]), -sin(-RPY[2]), 0],
        [sin(-RPY[2]), cos(-RPY[2]), 0],
        [0, 0, 1]
        ]
    vector = np.transpose(vec)
    result = Rx @ vector
    result = Ry @ result
    result = Rz @ result
    #print(result)
    return result
    
    
    

gravity = [0, 0, -9.81]


for iteration in range(1):
    datasetEntry = np.load("Dataset/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
    #total accelaration at each simulation step
    totalAcceleration = -datasetEntry[10][:] + gravity #world frame of reference
    #print(totalAcceleration[7070] - datasetEntry[10][7070])
    #print(datasetEntry[8][1:10])
    forceInGraspFOR = np.zeros((24000,3))
    for q in range(24000):
        forceInGraspFOR[q] = inverseRPYrotation(totalAcceleration[q],p.getEulerFromQuaternion(datasetEntry[8][q])) # args are total force in world frame, and orientation of end effector in world frame 
        #print(forceInGraspFOR[q])
    
print("Payload Orientation")
print(datasetEntry[8][18000:18100])
print()
print()    
print("Payload Velocity")
print(datasetEntry[9][18000:18100])
print()
print()  
print("Payload Acceleration")
print(datasetEntry[10][18000:18100])
print()
print()
print("Total Acceleration")
print(totalAcceleration[18000:18100])
print()
print()   
print("Total Acceleration Grasp FOR") 
print(forceInGraspFOR[18000:18100])
#print(forceInGraspFOR[15000])




#RPYroatation([1,1,0],[1.57,0,0])
#RPYroatation([1,1,0],[0,1.57,0])
#inverseRPYrotation([1,1,0],[0, 1.57, 1.57])


