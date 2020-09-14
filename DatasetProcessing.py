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
    # sign @ is a matrix multiplication
    vector = np.transpose(vec)
    result = Rx @ vector
    result = Ry @ result
    result = Rz @ result
    #print(result)
    return result

#Returns [theta, phi, r]
def CartesianToSpherical10deg(vec):
    theta = atan2(vec[1],vec[0])
    phi = atan2(((vec[0]*vec[0] + vec[1]*vec[1])**0.5),vec[2])
    r = (vec[0]*vec[0] + vec[1]*vec[1] + vec[2]*vec[2])**0.5
    # go to degrees
    theta = theta/3.14*180
    phi = phi/3.14*180
    #now take care of resolution
    theta = int(int((theta-5))/int(10))
    phi = int(int((phi-5))/int(10))
    force = [theta, phi, r]
    #print(force)
    return force
    
    
    
    
    

gravity = [0, 0, -9.81]
fail_count = 0

for iteration in range(6000):
    print("Processing dataset Entry: " + str(iteration))
    datasetEntry = np.load("Dataset/TestEntry" + str(iteration) + ".npy", allow_pickle = True)
    #print(datasetEntry)
    #check for unwated collisions
    #print()
    #print(datasetEntry[0])
    if datasetEntry[12] == 1:
    #total accelaration at each simulation step
        totalAcceleration = -datasetEntry[10][:] + gravity #world frame of reference
        #print(totalAcceleration[7070] - datasetEntry[10][7070])
        #print(datasetEntry[8][1:10])
        forceInGraspFOR = np.zeros((24000,3))
        for q in range(24000):
            forceInGraspFOR[q] = inverseRPYrotation(totalAcceleration[q],p.getEulerFromQuaternion(datasetEntry[8][q])) # args are total force in world frame, and orientation of end effector in world frame 
            #print(forceInGraspFOR[q])
            #Now make the force in form that allows for choosing a threshold
            forceInGraspFOR[q] = CartesianToSpherical10deg(forceInGraspFOR[q])
        newData = [datasetEntry[0],datasetEntry[1],datasetEntry[2],datasetEntry[3],datasetEntry[4],datasetEntry[5],datasetEntry[6],datasetEntry[7],datasetEntry[8],datasetEntry[9],datasetEntry[10],datasetEntry[11],datasetEntry[12], forceInGraspFOR]
        print(len(newData[0]))
        entryName = "TestEntry" + str(iteration-fail_count) + ".npy"
        fileName = "ProcessedDataset/" + entryName
        np.save(fileName, newData)
    else:
        fail_count = fail_count + 1
        
    
#print("Payload Orientation")
#print(datasetEntry[8][18000:18100])
#print()
#print()    
#print("Payload Velocity")
#print(datasetEntry[9][18000:18100])
#print()
#print()  
#print("Payload Acceleration")
#print(datasetEntry[10][18000:18100])
#print()
#print()
#print("Total Acceleration")
#print(totalAcceleration[18000:18100])
#print()
#print()   
#print("Total Acceleration Grasp FOR") 
#print(forceInGraspFOR[18000:18100])
##print(forceInGraspFOR[15000])




#RPYroatation([1,1,0],[1.57,0,0])
#RPYroatation([1,1,0],[0,1.57,0])
#inverseRPYrotation([1,1,0],[0, 1.57, 1.57])


