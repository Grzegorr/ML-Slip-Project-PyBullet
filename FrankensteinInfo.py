#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim
from Grasping import Grasping as Grasp

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
TheArm = p.loadURDF("Models/Frankenstein/FrankensteinV2.urdf",cubeStartPos, cubeStartOrientation,useFixedBase = 1)

print("Number of joints in the Frankenstein: " + str(p.getNumJoints(TheArm)))

for joint_index in range(0,p.getNumJoints(TheArm)):
    print()
    info = p.getJointInfo(TheArm,joint_index)
    print("Joint index: " + str(info[0]))
    print("Joint name: " + str(info[1]))
    print("Joint type: " + str(info[2]))
    print()

#G = Grasp(p,TheArm)
#G.stiffFingerClosePosition(90)
    
G = Grasp(p,TheArm)
G.spreadFingers(45)


#'closing hand'
#p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=11, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1) 
#p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=17, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1) 
#p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=22, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1) 

#'spreading fingers'
#p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=10, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1) 
#p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=16, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1) 



p.setRealTimeSimulation(1)

time.sleep(10)