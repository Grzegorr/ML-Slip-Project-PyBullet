#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim
from Grasping import Grasping as Grasp
import Interface
from ArmController import ArmController

#Connet to the API
physicsClient = p.connect(p.GUI)

#Path to defaultyly downloaded data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Setting the gravity
p.setGravity(0,0,-10)

#Load-in a plane
planeId = p.loadURDF("plane.urdf")

cubeStartPos = [0,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
#TheArm = p.loadURDF("Models/Frankenstein/FrankensteinV2.urdf",cubeStartPos, cubeStartOrientation,useFixedBase = 1)
TheArm = p.loadURDF("Models/Frankenstein/new/FrankensteinV3.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)

cubeStartPos = [0.5, 0, 0.2]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
Obj4 = p.loadURDF("Models/PhysicsTesting/small_sphere.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)

    
#Grasping class
G = Grasp(p,TheArm)
I = Interface.Interface()
AC = ArmController(p,TheArm)


#Run the simulation
for i in range (0,200000):
    if i % 100 == 0:
        print("Step" + str(i))
    AC.IKiteration([0.5,0.3,0.5], p.getQuaternionFromEuler([1.57,0,0]), i, 0,500)
    AC.IKiteration([0.7,0.3,0.2], p.getQuaternionFromEuler([1.57,0,0]), i, 500,1000)
    AC.IKiteration([0.5,0.2,0.2], p.getQuaternionFromEuler([1.57,0,0]), i, 1000,1500)
    AC.IKiteration([0.5,0.1,0.2], p.getQuaternionFromEuler([1.57,0,0]), i, 1500,2000)
    AC.IKiteration([0.5,0.02,0.2], p.getQuaternionFromEuler([1.57,0,0]), i, 2000,2500)
    if i == 2500:
        AC.frankaJointsLock()
    if i % 4000 <= 2000 and i > 2500:
        G.closeHandTorques()
        G.spreadFingers(60)
    if i % 4000 > 2000 and i > 2500:
        G.openHandTorques()
        G.spreadFingers(60)
    if i % 40 == 0:
        proximal1, proximal2, proximal3, distal1, distal2, distal3 = G.readTactile()
        I.updateWindow(proximal1, proximal2, proximal3, distal1, distal2, distal3)    
    p.stepSimulation()
    time.sleep(1./240.)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    