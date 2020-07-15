#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim
from Grasping import Grasping as Grasp
#import Interface
from ArmController import ArmController
from Statistics import Statistics as Stats
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time
from KlasaCina import KC
from math import *



#Can be done by detecting closed fingers probably
def graspFailFlag():
    finger1pos = p.getJointState(TheArm,11)[0]
    finger2pos = p.getJointState(TheArm,28)[0]
    finger3pos = p.getJointState(TheArm,44)[0]
    if finger1pos > 3.13 or finger2pos > 3.13 or finger3pos > 3.13:
        if i > 6500:
            return 1
    else:
        return 0 


#degrees used instead of radians
#vec = [r,theta, phi]
#def PolarToCartesian(vec):
#    theta = vec[1]
#    phi = vec[2]
#    theta = theta/180.0*3.14
#    phi = phi/180.0*3.14
#    x = r * sin(phi) * cos(theta)
#    y = r * sin(phi) * sin(theta)
#    z = r * cos(phi)
#    return [x,y,z]

def PolarToCartesian(vec):
    theta = vec[1]
    phi = vec[2]
    theta = theta/180.0*3.14
    phi = phi/180.0*3.14
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return [x,y,z]

failFlag = np.zeros(24000)

#physicsClient = p.connect(p.GUI)
physicsClient = p.connect(p.DIRECT)

calibrationOutput = np.zeros((36,18))

for theta_seed in range(36):
    for phi_seed in range(18):
        iteration = 18 * theta_seed + phi_seed 
        i = 0
        task = np.load("Tasks/Calibration.npy", allow_pickle = True) 
    
        
        
        #Path to defaultyly downloaded data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        
        #Setting the gravity
        p.setGravity(0,0,-0.1)
        
        #Load-in a plane
        planeId = p.loadURDF("plane.urdf")
        
        cubeStartPos = [0,0,0]
        cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
        #TheArm = p.loadURDF("Models/Frankenstein/FrankensteinV2.urdf",cubeStartPos, cubeStartOrientation,useFixedBase = 1)
        TheArm = p.loadURDF("Models/Frankenstein/new/FrankensteinV3.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)
        
        cubeStartPos = [0.5,0,-0.1]
        cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
        table = p.loadURDF("Models/PhysicsTesting/table.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)
        
        
        cubeStartPos = [0.5,0,0.17]
        cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
        #payload = p.loadURDF("Models/PhysicsTesting/cylinder.urdf",cubeStartPos, cubeStartOrientation)
        #payload = p.loadURDF("Models/PhysicsTesting/cylinder2.urdf",cubeStartPos, cubeStartOrientation)
        payload = p.loadURDF("Models/PhysicsTesting/cylinder3.urdf",cubeStartPos, cubeStartOrientation)
        
        #Grasping class
        G = Grasp(p,TheArm)
        #I = Interface.Interface()
        AC = ArmController(p,TheArm)
        S = Stats()
        G.lockSpreadFingersJoints()
        czas = KC()
        
        while(i in range (0,24000)):
            failFlag[i] = graspFailFlag()
            
            if i % 1000 == 0:
                print("Iteration: " + str(iteration) + ", Step: " + str(i))
                
            #Setting direction and increaring gravity    
            if i % 100 == 0 and i > 10000: 
                r = 0.05*(i-10000)
                gravity = PolarToCartesian([r,10* theta_seed, 10* phi_seed])
                p.setGravity(gravity[0], gravity[1], gravity[2])
            
            AC.GrabbingSequence(i,0,G)
            AC.runSeriesOfIKTasks(i,task)
            
            if i == 23999:   
                print()
                print("It was iteration no. " + str(iteration) + ". The gravity vector was: " + str(gravity) + ". Theta_seed was: " + str(theta_seed) + ". Phi_seed was " + str(phi_seed) + ".")
                print()
                p.resetSimulation()
                #print(np.where(failFlag == 1)[0][0])
                if len(np.where(failFlag == 1)[0]) == 0:
                    #print("No grasp fail")
                    failedGraspStep = 24000
                else:
                    failedGraspStep = np.where(failFlag == 1)[0][0]
                resultingAcceleration = 0.05*(failedGraspStep-10000)
                calibrationOutput[theta_seed][phi_seed] = resultingAcceleration
                
            p.stepSimulation()   
            i = i + 1

entryName = "Calibration2.npy"
fileName = "Calibration/" + entryName
np.save(fileName, calibrationOutput)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
