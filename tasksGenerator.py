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
    #boundries = [timeDifference,position, orientation,]
    boundries = [ [100,1000], [[-0.6, -0.6, 0.4],[0.6 ,0.6, 1.2]], [[-3.14, -3.14, -3.14],[3.14, 3.14, 3.14]], [0,2], [0,2], [0,2], [0,2] ] 
    task = []
    startTime = firstStartStep
    while(1):
        #randomly generated changes
        timeChange = boundries[0][0] + random.random() * ( boundries[0][1] - boundries[0][0])
        startTime = int(startTime + timeChange)
        position = [random.random() * ( boundries[1][1][0] - boundries[1][0][0]), random.random() * ( boundries[1][1][1] - boundries[1][0][1]), random.random() * ( boundries[1][1][2] - boundries[1][0][2]) ]
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
    #print(task)
    
def multipleRandomTaskGenerator(noOfTasks):
    for x in range(noOfTasks):
        autoTaskGenerator(x)
        
        


multipleRandomTaskGenerator(1000)
testTasksGenerate()

















