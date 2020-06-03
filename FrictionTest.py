#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pybullet as p
import time
import pybullet_data
import pybullet_robots.panda.panda_sim as panda_sim
from Grasping import Grasping as Grasp

#degree to rads
ratio = 3.14/180.0

#Connet to the API
physicsClient = p.connect(p.GUI)

#Path to defaultyly downloaded data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Setting the gravity
p.setGravity(0,0,-10)

#Load-in a plane
planeId = p.loadURDF("plane.urdf")

cubeStartPos = [0,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,30*ratio,0*ratio])
Obj1 = p.loadURDF("Models/PhysicsTesting/slope.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)

cubeStartPos = [0,2,0]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,30*ratio,0*ratio])
Obj2 = p.loadURDF("Models/PhysicsTesting/slope2.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)

cubeStartPos = [-1,2,2]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,0*ratio,0*ratio])
Obj3 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-1,0,2]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,0*ratio,0*ratio])
Obj4 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-5, 0.03, 0]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,0*ratio,0*ratio])
Obj4 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-5, 0.07, 0.3]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,0*ratio,0*ratio])
Obj4 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-5, -0.03, 0.6]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,0*ratio,0*ratio])
Obj4 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-5, 0.03, 1]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,0*ratio,0*ratio])
Obj4 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)

cubeStartPos = [-5, -0.05, 2]
cubeStartOrientation = p.getQuaternionFromEuler([0*ratio,0*ratio,0*ratio])
Obj4 = p.loadURDF("Models/PhysicsTesting/box.urdf",cubeStartPos, cubeStartOrientation)





#Run the simulation
for i in range (2000):
    p.stepSimulation()
    time.sleep(1./240.)

#Disconnect and close the simulation
p.disconnect()

















