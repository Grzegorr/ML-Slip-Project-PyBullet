#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim
import numpy as np

#max speeds
maxSpeed = 0.1
timeStep = 1./240.


def waypointToTimestamp(maxSpeed,timeStamp, waypoints):
    noWay = len(waypoints)
    timestamps = np.zeros(noWay)
    timestamps[0] = 240
    for t in range(1,noWay):
        timestamps[t] = timestamps[t-1] + abs(waypoints[t][0]-waypoints[t-1][0])*240./maxSpeed
    return timestamps
  
    
def moveJoint(pos):
    p.setJointMotorControl2(bodyUniqueId=TheArm, jointIndex=1, controlMode=p.POSITION_CONTROL, targetPosition = pos, maxVelocity = maxSpeed) 

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

#Waypoints
waypoints = [
[0],
[0.5],
[-0.5],
[0.5],
[-0.5],
[0.5],
[-0.5]
]

timestamps = waypointToTimestamp(maxSpeed, timeStep, waypoints)
print()
print(timestamps)
print()

#Run the simulation
count = 0;
for i in range (20000):
    if timestamps[count] == i:
        #print(p.getJointState(TheArm,1))
        moveJoint(waypoints[count+1][0])
        count = count + 1
    p.stepSimulation()
    time.sleep(timeStep)

#Disconnect and close the simulation
p.disconnect()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    