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
  
    
def moveJoint(pos,index,armName):
    p.setJointMotorControl2(bodyUniqueId=armName, jointIndex=index, controlMode=p.POSITION_CONTROL, targetPosition = pos, maxVelocity = maxSpeed) 

def moveArm(pos):
    p.setJointMotorControlArray(bodyUniqueId=TheArm, jointIndices = [0,1,2,3,4,5,6], controlMode = p.POSITION_CONTROL, targetPositions = pos, maxVelocities = [0.1,0.1,0.1,0.1,0.1,0.1,0.1])

def moveArmMaxSpeed(pos, armName):
    moveJoint(pos[0],0,armName)
    moveJoint(pos[1],1,armName)
    moveJoint(pos[2],2,armName)
    moveJoint(pos[3],3,armName)
    moveJoint(pos[4],4,armName)
    moveJoint(pos[5],5,armName)
    moveJoint(pos[6],6,armName)

#Connet to the API
physicsClient = p.connect(p.GUI)

#Path to defaultyly downloaded data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Setting the gravity
p.setGravity(0,0,-9.81)

#Load-in a plane
planeId = p.loadURDF("plane.urdf")

#Spawn multiple robots in given places
robot_spawns = [
['TheArm', [0,0,0], [0,0,0]],
['TheArm2', [1,0,0], [0,0,0]],
['TheArm3', [2,0,0], [0,0,0]]
]
for i in robot_spawns:
    cubeStartPos = i[1]
    cubeStartOrientation = p.getQuaternionFromEuler(i[2])
    print(i[0])
    exec(f'{i[0]} = p.loadURDF("franka_panda/panda.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)')

#Information about the setup
print('')
print('Number of joints')
print(p.getNumJoints(TheArm))
print('')

#Waypoints
waypoints = [
[0,0,0,0,0,0,0],
[0.5,0.5,0.5,0.5,0.5,0.5,0.5],
[-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5],
[0.5,0.5,0.5,0.5,0.5,0.5,0.5],
[-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5],
[0.5,0.5,0.5,0.5,0.5,0.5,0.5],
[-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5]
]
for i in robot_spawns:
    exec(f'waypoints{i[0]} = waypoints')
    exec(f'timestamps{i[0]} = waypointToTimestamp(maxSpeed, timeStep, waypoints{i[0]})')
    exec(f'count{i[0]} = 0')

#Run the simulation
for i in range (20000):
    for i in robot_spawns:
        if eval('count{i[0]} < (len(timestamps{i[0]}) - 1)'):
            if eval('timestamps{i[0]}[count{i[0]}] == i'):
                exec(f'moveArmMaxSpeed(waypoints{i[0]}[count{i[0]}+1], {i[0]})')
                exec(f'count{i[0]} = count{i[0]} + 1')
    p.stepSimulation()
    time.sleep(timeStep)

#Disconnect and close the simulation
p.disconnect()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    