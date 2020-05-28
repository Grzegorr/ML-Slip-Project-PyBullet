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
p.setGravity(0,0,-9.81)

#Load-in a plane
planeId = p.loadURDF("plane.urdf")

#Spawn a robot in a given place
cubeStartPos = [0,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
TheArm = p.loadURDF("franka_panda/panda.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)

#Move
p.setJointMotorControl2(bodyUniqueId=TheArm, 
jointIndex=1, 
controlMode=p.POSITION_CONTROL, 
targetPosition = 0.5,
maxVelocity = 0.1) 


#Run the simulation
for i in range (2000):
    p.stepSimulation()
    time.sleep(1./240.)

#Disconnect and close the simulation
p.disconnect()
  
