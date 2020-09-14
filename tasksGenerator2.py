#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:38:14 2020

@author: grzegorz
"""
import pybullet as p
import numpy as np
import random

#[startStep, position, orientation, targetVelocity, maxVelocity, velocityGain, positionGaing]

def testTasksGenerate():
    task = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([0,0,0]), 0, 0.1, 0.1, 0.1 ]
            ]
    entryName = "Calibration.npy"
    fileName = "Tasks/" + entryName
    np.save(fileName, task)
    
    task = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), 0, 1, 1, 1 ],
              [ 7000, [0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ],
              [ 7500, [0.5,0.5,0.6], p.getQuaternionFromEuler([-1.57,0,0]), 1, 1, 1, 1 ],
              [ 8000, [0.3,0.3,0.3], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ],
              [ 8500, [0.5,0.5,0.6], p.getQuaternionFromEuler([0,0,0]), 1, 1, 1, 1 ]
            ]
    entryName = "ArmHitTable.npy"
    fileName = "Tasks/" + entryName
    np.save(fileName, task)
    
    task = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), 0, 1, 1, 1 ],
              [ 7000, [0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ],
              [ 7500, [0.5,0.5,0.6], p.getQuaternionFromEuler([-1.57,0,0]), 1, 1, 1, 1 ],
              [ 8000, [0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ],
              [ 8500, [0.5,0,0.2], p.getQuaternionFromEuler([1.57,0,0]), 0, 1, 1, 1 ]
              ]
              
    entryName = "PayloadHitTable.npy"
    fileName = "Tasks/" + entryName
    np.save(fileName, task)
    
    task = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), 0, 1, 1, 1 ],
              [ 7000, [0.5,-0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ],
              [ 7500, [0.5,0.5,0.6], p.getQuaternionFromEuler([-1.57,0,0]), 1, 1, 1, 1 ],
              [ 8000, [0.5,0.5,0.0], p.getQuaternionFromEuler([0,0,0]), 1, 1, 1, 1 ]
            ]
    entryName = "ArmHitFloor.npy"
    fileName = "Tasks/" + entryName
    np.save(fileName, task)
    
    task = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), 0, 1, 1, 1 ]
            ]
    entryName = "SuccessfulLift.npy"
    fileName = "Tasks/" + entryName
    np.save(fileName, task)
    
    task = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), 3, 1, 2, 2 ]
            ]
    entryName = "FailedLift.npy"
    fileName = "Tasks/" + entryName
    np.save(fileName, task)


def autoTaskGenerator(genTaskConter):
    #task = [startStep, position, orientation, targetVelocity, maxVelocity, velocityGain, positionGaing]
    firstStartStep = 6500
    previousPos = [0.5,0,0.5]
    #boundries = [timeDifference,position, orientation,]
    boundries = [ [100,1000], [[-0.1, -0.1, -0.1],[0.1 ,0.1, 0.1]], [[-3.14, -3.14, -3.14],[3.14, 3.14, 3.14]], [0,0.6], [0,0.6], [0,0.6], [0,0.6] ] 
    task = []
    startTime = firstStartStep
    while(1):
        #randomly generated changes
        timeChange = 500
        startTime = int(startTime + timeChange)
        positionChange = [random.random() * ( boundries[1][1][0] - boundries[1][0][0]), random.random() * ( boundries[1][1][1] - boundries[1][0][1]), random.random() * ( boundries[1][1][2] - boundries[1][0][2]) ]
        position = np.array(previousPos) + np.array(positionChange)
        evaluatePos = position[0] >-0.7 and position[0] <0.7 and position[1] >-0.7 and position[1] <0.7 and position[2] >0.3 and position[2] <1.2 
        while(evaluatePos == 0):
            positionChange = [random.random() * ( boundries[1][1][0] - boundries[1][0][0]), random.random() * ( boundries[1][1][1] - boundries[1][0][1]), random.random() * ( boundries[1][1][2] - boundries[1][0][2]) ]
            position = np.array(previousPos) + np.array(positionChange)
            evaluatePos = position[0] >-0.7 and position[0] <0.7 and position[1] >-0.7 and position[1] <0.7 and position[2] >0.3 and position[2] <1.2 
            if evaluatePos == 0:
                position = np.array(previousPos) - np.array(positionChange)
                evaluatePos = position[0] >-0.7 and position[0] <0.7 and position[1] >-0.7 and position[1] <0.7 and position[2] >0.3 and position[2] <1.2 
                
        previousPos = position
        orientation = p.getQuaternionFromEuler([random.random() * ( boundries[2][1][0] - boundries[2][0][0]), random.random() * ( boundries[2][1][1] - boundries[2][0][1]), random.random() * ( boundries[2][1][2] - boundries[2][0][2]) ])
        tagetVelocity = random.random() * ( boundries[3][1] - boundries[3][0])
        maxVelocity = random.random() * ( boundries[4][1] - boundries[4][0])
        velocityGain = random.random() * ( boundries[5][1] - boundries[5][0])
        positionGain = random.random() * ( boundries[6][1] - boundries[6][0])
        
        if startTime > 24000:
            entryName = "PGTtest" + str(genTaskConter) + ".npy"
            fileName = "Tasks/" + entryName
            np.save(fileName, task)
        
            break
        
        waypoint = [startTime, position, orientation, tagetVelocity, maxVelocity, velocityGain, positionGain]
        task.append(waypoint)
    #print(task[1])
    #print()
    #print(len(task))
    
def multipleRandomTaskGenerator(noOfTasks):
    for x in range(noOfTasks):
        autoTaskGenerator(x)
        
        


multipleRandomTaskGenerator(200)
testTasksGenerate()

















