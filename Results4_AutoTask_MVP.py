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

cubeStartPos = [0.5,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
#TheArm = p.loadURDF("Models/Frankenstein/FrankensteinV2.urdf",cubeStartPos, cubeStartOrientation,useFixedBase = 1)
table = p.loadURDF("Models/PhysicsTesting/table.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)


cubeStartPos = [0.5,0,0.27]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
#TheArm = p.loadURDF("Models/Frankenstein/FrankensteinV2.urdf",cubeStartPos, cubeStartOrientation,useFixedBase = 1)
payload = p.loadURDF("Models/PhysicsTesting/cylinder.urdf",cubeStartPos, cubeStartOrientation)

    
#Grasping class
G = Grasp(p,TheArm)
I = Interface.Interface()
AC = ArmController(p,TheArm)
S = Stats()
G.lockSpreadFingersJoints()


#Run the simulation
for i in range (0,240000):
    if i % 100 == 0:
        print("Step" + str(i))
        
        
        
    AC.IKiteration([0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 6100,6500)
    AC.IKiteration([0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 6500,7000)
    AC.IKiteration([0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 7500,8000)
    AC.IKiteration([0,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 8000,8500)
    AC.IKiteration([0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 8500,9000)
    AC.IKiteration([0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 9000,9500)
    #AC.IKiteration([-0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 8500,9000)
    #AC.IKiteration([0.5,0,0.6], p.getQuaternionFromEuler([0,0,0]), i, 6500,7000)
    #AC.IKiteration([0.5,0,0.6], p.getQuaternionFromEuler([0,0,1.57]), i, 7000,6500) 
    #if i == 10000:
        #AC.frankaJointsUnlock()
    if i > 10000 and i % 2000 > 1000:
        AC.rollLastJoint(1.0)
    if i > 10000 and i % 2000 < 1000:
        AC.rollLastJoint(3.0)
    
    AC.GrabbingSequence(i,0,G)
    
    if i % 24 == 0 and i>6000:
        proximal1, proximal2, proximal3, distal1, distal2, distal3 = G.readTactile()
        I.updateWindow(proximal1, proximal2, proximal3, distal1, distal2, distal3)   
        proximal1, proximal2, proximal3, distal1, distal2, distal3 = G.readTactileFull()
        S.readWrenches(i, proximal1, proximal2, proximal3, distal1, distal2, distal3)
        forces = G.readJointsHand()
        print(forces)
        S.gatherJointHands(i,forces)
    p.stepSimulation()
    if i > 9000:
        time.sleep(1./240.)
    
    if i % 500 == 0:
        #S.printForcesX(i)
        S.printForcesHand(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    