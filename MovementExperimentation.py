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
#TheArm = p.loadURDF("Models/Frankenstein/FrankensteinV2.urdf",cubeStartPos, cubeStartOrientation,useFixedBase = 1)
TheArm = p.loadURDF("Models/Frankenstein/new/FrankensteinV3.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)

cubeStartPos = [0, 0, 3]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
Obj4 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)

    
    
    
for joint_index in range(0,p.getNumJoints(TheArm)):
    print()
    info = p.getJointInfo(TheArm,joint_index)
    print("Joint index: " + str(info[0]))
    print("Joint name: " + str(info[1]))
    print("Joint type: " + str(info[2]))
    print()
    
p.enableJointForceTorqueSensor(TheArm,50)

for i in range (-10000,20000):
#    if i%100 == 0:
#        print(max(p.getJointState(TheArm,50)[2]))
    if max(p.getJointState(TheArm,50)[2]) > 0.001:
        print(p.getJointState(TheArm,50)[2])
    p.stepSimulation()
    time.sleep(1./240.)

#Grasping class
G = Grasp(p,TheArm)

p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=5, controlMode=p.POSITION_CONTROL, targetPosition = 2, maxVelocity = 1)

#Run the simulation
for i in range (-10000,20000):
    if i == -9500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1)
    if i == -8500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 0,maxVelocity = 1) 
    if i == -7500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1)
    if i == -6500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 0,maxVelocity = 1)
    if i == -5500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1)
    if i == -4500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 0,maxVelocity = 1) 
    if i == -3500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 3,maxVelocity = 1)
    if i == -2500:
        p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=24, controlMode=p.POSITION_CONTROL, targetPosition = 0,maxVelocity = 1)
    if i == 500:
        G.spreadFingers(0)
    if i == 1000:
        G.spreadFingers(90)
    if i == 1500:
        G.spreadFingers(0)
    if i == 2000:
        G.spreadFingers(90)
    if i == 2500:
        G.spreadFingers(0)
    if i == 3000:
        G.spreadFingers(45)
    if i == 3500:
        G.spreadFingers(0)
    if i == 4000:
        G.stiffFingerClosePosition(180)
    if i == 5000:
        G.stiffFingerClosePosition(0)
    if i == 6000:
        G.stiffFingerClosePosition(180)
    if i == 7000:
        G.stiffFingerClosePosition(0)
    if i == 8000:
        G.stiffFingerClosePosition(90)
    if i == 9000:
        G.stiffFingerClosePosition(0)
    if i == 10000:
        G.stiffFingerClosePosition(90)
    if i == 11000:
        G.stiffFingerClosePosition(0)
    if i == 12000:
        G.stiffFingerClosePosition(180)
        G.spreadFingers(90)
    if i == 13000:
        G.stiffFingerClosePosition(0)
        G.spreadFingers(0)
    if i == 14000:
        G.stiffFingerClosePosition(180)
        G.spreadFingers(90)
    p.stepSimulation()
    time.sleep(1./240.)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    