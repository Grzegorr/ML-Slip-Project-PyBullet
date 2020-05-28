#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data

#Connet to the API
physicsClient = p.connect(p.GUI)

#Path to defaultyly downloaded data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

print(pybullet_data.getDataPath())

#Setting the gravity
p.setGravity(0,0,-10)

#Load-in a plane
planeId = p.loadURDF("plane.urdf")

#Spawn a robot in a given place
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,3]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId2 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,5]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId3 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,7]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId4 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,9]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId5 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,11]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId6 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,13]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId7 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,15]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId8 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,17]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId9 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,19]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId10 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,21]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId11 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,23]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId12 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,25]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId13 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

#Spawn a robot in a given place
cubeStartPos = [0,0,27]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId14 = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
    
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()








