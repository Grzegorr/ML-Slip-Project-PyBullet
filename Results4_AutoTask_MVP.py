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
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time



def allStatsHandling():
    if i % 24 == 0 and i > 0:
        proximal1, proximal2, proximal3, distal1, distal2, distal3 = G.readTactile()
        #I.updateWindow(proximal1, proximal2, proximal3, distal1, distal2, distal3)   
        proximal1, proximal2, proximal3, distal1, distal2, distal3 = G.readTactileFull()
        S.readWrenches(i, proximal1, proximal2, proximal3, distal1, distal2, distal3)
        forces = G.readJointsHand()
        #print(forces)
        S.gatherJointHands(i,forces)
        
    S.failFlag[i] = graspFailFlag()   
    S.unwantedCollisionFlag[i] = unwantedCollisionFlag()
 

    linkWorldOrientation, worldLinkLinearVelocity = G.readPayloadState() # reads the orientation and velocity of a payload using a dummy link to estimate it
    S.readPayloadState(i,linkWorldOrientation, worldLinkLinearVelocity)
    if i == 23999:
        S.computeAcceleration("False")
        S.printFlags("True")
        S.datasetEntryPrepareAndSave(task)
        
def unwantedCollisionFlag():
    contactPoints = p.getContactPoints()
    for point in contactPoints:
        if point[2] == 3:  ##payload part of the contact
            if point[1] == 0 or (point[1] == 1 and point[3] < 7) or point[1] == 2:
                #print(point)
                #print()
                if i > 6500:
                    return 1
        if point[1] == 0 and point[2] == 1 and point[4] > 1: #arm hitting ground
            if i > 6500:
                    return 1
        if point[1] == 1 and point[2] == 2: #arm hits table
            if i > 6500:
                    return 1
            
    return 0

#Can be done by detecting closed fingers probably
def graspFailFlag():
    finger1pos = p.getJointState(TheArm,11)[0]
    finger2pos = p.getJointState(TheArm,28)[0]
    finger3pos = p.getJointState(TheArm,44)[0]
    if finger1pos > 3.13 or finger2pos > 3.13 or finger3pos > 3.13:
        if i > 6500:
            return 1
    else:
        return 0 
    
        
#tasks[x]= [simStepStart, positionEndEffector, orientationEndEffector, targetVel,maxVel, Vgain, Pgain]  
        #AC.IKiterationAuto([0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 6100,6500,0,1,1,1)
#tasks = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), 0, 1, 1, 1 ],
#          [ 7000, [0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ],
#          [ 7500, [0.5,0.5,0.6], p.getQuaternionFromEuler([-1.57,0,0]), 1, 1, 1, 1 ],
#          [ 8000, [0.3,0.3,0.3], p.getQuaternionFromEuler([-1.57,0,0]), 1, 1, 1, 1 ],
#          [ 8500, [0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ]
#        ]
        
task = np.load("Tasks/ArmHitTable.npy", allow_pickle = True)        
        
    
    
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
table = p.loadURDF("Models/PhysicsTesting/table.urdf",cubeStartPos, cubeStartOrientation, useFixedBase = 1)


cubeStartPos = [0.5,0,0.27]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
payload = p.loadURDF("Models/PhysicsTesting/cylinder.urdf",cubeStartPos, cubeStartOrientation)

    
#Grasping class
G = Grasp(p,TheArm)
I = Interface.Interface()
AC = ArmController(p,TheArm)
S = Stats()
G.lockSpreadFingersJoints()


#Run the simulation
for i in range (0,24000):
    if i % 100 == 0:
        print("Step" + str(i))
        
    AC.GrabbingSequence(i,0,G)
    AC.runSeriesOfIKTasks(i,task)
    
    allStatsHandling()
    p.stepSimulation()
    #if i > 8630:
        #time.sleep(1./240.)
        #time.sleep(1./40.)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
#    AC.IKiterationAuto([0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 6100,6500,0,1,1,1)
#    AC.IKiterationAuto([0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 6500,7000,0,1,1,1)
#    AC.IKiterationAuto([0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 7500,8000,1,1,1,1)
#    AC.IKiterationAuto([0,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 8000,8500,1,1,1,1)
#    AC.IKiterationAuto([0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 8500,9000,1,1,1,1)
#    AC.IKiterationAuto([0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 9000,9500,1,1,1,1)
#    #AC.IKiteration([-0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), i, 8500,9000)
#    #AC.IKiteration([0.5,0,0.6], p.getQuaternionFromEuler([0,0,0]), i, 6500,7000)
#    #AC.IKiteration([0.5,0,0.6], p.getQuaternionFromEuler([0,0,1.57]), i, 7000,6500) 
#    #if i == 10000:
#        #AC.frankaJointsUnlock()
#    if i > 10000 and i % 2000 > 1000:
#        AC.rollLastJoint(3)
#    if i > 10000 and i % 2000 < 1000:
#        AC.rollLastJoint(-3)

    
#    if i % 500 == 0:
#        S.printForcesX(i)
#        S.printForcesHand(i)
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
#        imghight = 2
#        imgwidth = 4
#        stateLink = p.getLinkState(TheArm, 60)
#        viewMatrix = p.computeViewMatrixFromYawPitchRoll(stateLink[0],3,0,0,0,2)
#        image = p.getCameraImage(imghight,imgwidth,viewMatrix)
#        image_three = []
#        #print(image[2])
#        
#        for n in range(len(image[2])):
#            if n % 4 == 0:
#                image_three.append([image[2][n],image[2][n+1],image[2][n+2]])
#        finalimg = np.zeros((imghight,imgwidth,3))
#        
#        #print(image_three)
#        
#        for n in range(len(image_three)):
#            finalimg[int(n/imgwidth)][int(n%imgwidth)][:] = image_three[n][:]
#        #print(image[2])
#        
#        #print(finalimg)
#        #print(type(image[2]))
#        #print(image[2])
#        #imgplot = plt.imshow([[[255,255,255],[0,0,0]],[[0,0,0],[255,255,255]]])
#        plt.figure()
#        plt.ion()
#        mgplot = plt.imshow(finalimg/256.0)
#        plt.show()
#        time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    