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

    
    
    
for joint_index in range(0,p.getNumJoints(TheArm)):
    print()
    info = p.getJointInfo(TheArm,joint_index)
    print("Joint index: " + str(info[0]))
    print("Joint name: " + str(info[1]))
    print("Joint type: " + str(info[2]))
    print()
    
#Grasping class
G = Grasp(p,TheArm)
I = Interface.Interface()
AC = ArmController(p,TheArm)

#Run the simulation
for i in range (0,20000):
    AC.frankaJointsLock()
    if i % 20 == 0:
        proximal1, proximal2, proximal3, distal1, distal2, distal3 = G.readTactile()
        I.updateWindow(proximal1, proximal2, proximal3, distal1, distal2, distal3)
    if i % 5000 <= 2500:
        G.closeHandTorques()
        G.spreadFingers(60)
    if i % 5000 > 2500:
        G.openHandTorques()
        G.spreadFingers(60)
    p.stepSimulation()
    time.sleep(1./240.)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    