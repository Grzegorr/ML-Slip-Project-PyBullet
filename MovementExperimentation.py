#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim
from Grasping import Grasping as Grasp
import Interface

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

#LL, UL = G.returnLimits()
#IK = p.calculateInverseKinematics(TheArm,8,[0, 0.8, 0.2],targetOrientation = [0,0,0,0], lowerLimits = LL, upperLimits = UL) 
#IK = p.calculateInverseKinematics(TheArm,9,[0, 0.5, 0.5],targetOrientation = [0,0,1,0])  
#print(IK)
#for joint in range(0,7):
 #   p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=joint, controlMode=p.POSITION_CONTROL, targetPosition = IK[joint], maxVelocity = 1)

#for joint in [13,30,46]:
#    p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=joint, controlMode=p.POSITION_CONTROL, targetPosition = 1.7, maxVelocity = 1)
    
    
#p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=5, controlMode=p.POSITION_CONTROL, targetPosition = 2, maxVelocity = 1)

#Run the simulation
for i in range (0,200000):
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    