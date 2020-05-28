#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim

#Connet to the API
physicsClient = p.connect(p.GUI)

#Path to defaultyly downloaded data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Setting the gravity
p.setGravity(0,0,-10)

#Load-in a plane
planeId = p.loadURDF("plane.urdf")

#Spawn a robot in a given place
cubeStartPos = [-3,3,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("Models/PandaFamily/franka_panda/panda.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-2,2,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId2 = p.loadURDF("Models/PandaFamily/panda_no_gripper/panda.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-1,1,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId3 = p.loadURDF("Models/ll4ma_robots_description/urdf/reflex/model.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [5,1,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId4 = p.loadURDF("Models/ReFlex/ReFlex_BuildUp/model.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [0,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
TheArm = p.loadURDF("Models/Frankenstein/Frankenstein.urdf",cubeStartPos, cubeStartOrientation,useFixedBase = 1)


print(p.getNumJoints(boxId2))
print(p.getNumJoints(TheArm))
 

#Run the simulation
for i in range (20000):
    
    if i%500 == 0:
        print('Current simulation step: ' + str(i))
    
    if i == 1000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=0, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 2000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=1, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 3000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=2, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 4000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=3, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 5000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=4, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 6000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=5, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 7000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=6, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 8000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=7, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 9000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=8, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 10000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=9, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 11000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=10, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 12000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=11, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    if i == 13000:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=12, controlMode=p.POSITION_CONTROL, targetPosition = 2,maxVelocity = 1)
    p.stepSimulation()
    time.sleep(1./240.)

#Disconnect and close the simulation
p.disconnect()