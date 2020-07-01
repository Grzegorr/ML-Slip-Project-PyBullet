#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim
from Grasping import Grasping as Grasp
import Interface
from ArmController import ArmController
from Statistics import Statistics as Stats
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time
from KlasaCina import KC


#degrees used instead of radians
def PolarToCartesian(vec):


physicsClient = p.connect(p.GUI)

for iteration in range(2):
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
    payload = p.loadURDF("Models/PhysicsTesting/cylinder.urdf",cubeStartPos, cubeStartOrientation)
    
    #Grasping class
    G = Grasp(p,TheArm)
    #I = Interface.Interface()
    AC = ArmController(p,TheArm)
    S = Stats()
    G.lockSpreadFingersJoints()
    czas = KC()
    
    while(i in range (0,24000)):
        if i % 1000 == 0:
            print("Iteration: " + str(iteration) + ", Step: " + str(i))
        #Setting direction and increaring gravity    
        if i % 100 == 0 and i > 10000:    
            p.setGravity(0,0,0.01*(i-10000))
        
        AC.GrabbingSequence(i,0,G)
        AC.runSeriesOfIKTasks(i,task)
        
        if i == 23999:   
            p.resetSimulation()
            
        p.stepSimulation()   
        i = i + 1
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    