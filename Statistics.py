#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


class Statistics:
    
    def __init__(self):
        print("Using Statistics Class")
        
        self.proximal1 = np.zeros((1000,5,6))
        self.proximal2 = np.zeros((1000,5,6))
        self.proximal3 = np.zeros((1000,5,6))
        self.distal1 = np.zeros((1000,4,6))
        self.distal2 = np.zeros((1000,4,6))
        self.distal3 = np.zeros((1000,4,6))
        self.handForces = np.zeros((1000,6))
        
        self.unwantedCollisionFlag = np.zeros(24000)
        self.failFlag = np.zeros(24000)
        
        self.payloadOrientation = np.zeros((24000,4))
        self.payloadVelocity = np.zeros((24000,3))
        self.payloadAcceleration = np.zeros((24000,3))
        
    def readWrenches(self, simStep, proximal1, proximal2, proximal3, distal1, distal2, distal3):
        index = int(simStep/24)
        #print(proximal1)
        self.proximal1[index][:][:] = proximal1
        #print()
        #print()
        #print()
        #print(proximal1)
        #print(self.proximal1[index][:][:])
        #print(self.proximal1[:][:][2])
        #temp = self.proximal1[:,:,2]
        #print(temp.shape)
        self.proximal2[index][:][:] = proximal2
        self.proximal3[index][:][:] = proximal3
        self.distal1[index][:][:] = distal1
        self.distal2[index][:][:] = distal2
        self.distal3[index][:][:] = distal3
        #print(index)
        
    def printForcesX(self,simStep):
        index = int(simStep/24)
        plt.clf()
        plt.ion()
        #Distal
        plt.plot(abs(self.distal1[index-200:index,0,2]), label = "distal1_0")
        plt.plot(abs(self.distal1[index-200:index,1,2]), label = "distal1_1")
        plt.plot(abs(self.distal1[index-200:index,2,2]), label = "distal1_2")
        plt.plot(abs(self.distal1[index-200:index,3,2]), label = "distal1_3")
        
        plt.plot(abs(self.distal2[index-200:index,0,2]), label = "distal2_0")
        plt.plot(abs(self.distal2[index-200:index,1,2]), label = "distal2_1")
        plt.plot(abs(self.distal2[index-200:index,2,2]), label = "distal2_2")
        plt.plot(abs(self.distal2[index-200:index,3,2]), label = "distal2_3")
        
        plt.plot(abs(self.distal3[index-200:index,0,2]), label = "distal3_0")
        plt.plot(abs(self.distal3[index-200:index,1,2]), label = "distal3_1")
        plt.plot(abs(self.distal3[index-200:index,2,2]), label = "distal3_2")
        plt.plot(abs(self.distal3[index-200:index,3,2]), label = "distal3_3")
        
        plt.ylim(0.0, 0.5)
        
        
        plt.legend(bbox_to_anchor=(0, 1), loc='lower left', ncol = 3)
        plt.show()
        
    def printForce(self,simStep):
        index = int(simStep/24)
        plt.clf()
        plt.ion()
        #print(self.proximal1[:,0,0])
        #plt.plot(self.distal2[:,3,0], label = "X-force")
        #plt.plot(self.distal2[:,3,1], label = "Y-force")
        #plt.plot(self.distal2[:,3,2], label = "Z-force")
        #plt.plot(abs(self.distal1[:,2,0]), label = "X-force")
        #plt.plot(abs(self.distal1[:,2,1]), label = "Y-force")
        plt.plot(abs(self.distal1[:,2,2]), label = "Z-force")
        plt.legend(bbox_to_anchor=(0, 1), loc='lower left', ncol = 3)
        plt.xlim(index-200, index)
        plt.show()
        
    def gatherJointHands(self, simStep, forces):
        index = int(simStep/24)
        self.handForces[index] = forces
        
    def readPayloadState(self, simStep, linkWorldOrientation, worldLinkLinearVelocity):
        self.payloadOrientation[simStep][:] = linkWorldOrientation
        self.payloadVelocity[simStep][:] = worldLinkLinearVelocity
    
    #After simulation is finished, takes velocities and computes acceleration    
    def computeAcceleration(self,ifPrint):
        for x in range(1,len(self.payloadVelocity)):
            self.payloadAcceleration[x][0] = (self.payloadVelocity[x][0]-self.payloadVelocity[int(x-1)][0])*240.0
            self.payloadAcceleration[x][1] = (self.payloadVelocity[x][1]-self.payloadVelocity[int(x-1)][1])*240.0
            self.payloadAcceleration[x][2] = (self.payloadVelocity[x][2]-self.payloadVelocity[int(x-1)][2])*240.0
        if ifPrint == "True":
            plt.figure(1)
            plt.plot(self.payloadAcceleration[:,0], label = "Load accelecration X")
            plt.plot(self.payloadAcceleration[:,1], label = "Load accelecration Y")
            plt.plot(self.payloadAcceleration[:,2], label = "Load accelecration Z")
            plt.legend(bbox_to_anchor=(0, 1), loc='lower left', ncol = 3)
            plt.show()
            
    def printFlags(self, ifPrint):
        if ifPrint != "True":
            return
        plt.figure(2)
        plt.plot(self.unwantedCollisionFlag[6000:], label = "Unwanted Collision Flag")
        plt.plot(self.failFlag[6000:], label = "Grasp Failure Flag")
        plt.legend(bbox_to_anchor=(0, 1), loc='lower left', ncol = 2)
        plt.show()
            
        
        
    def printForcesHand(self,simStep):
        index = int(simStep/24)
        plt.clf()
        plt.ion()
        #Distal
        plt.plot(self.handForces[index-200:index,0], label = "proximal1")
        plt.plot(self.handForces[index-200:index,1], label = "distal1")
        plt.plot(self.handForces[index-200:index,2], label = "proximal2")
        plt.plot(self.handForces[index-200:index,3], label = "distal2")
        plt.plot(self.handForces[index-200:index,4], label = "proximal3")
        plt.plot(self.handForces[index-200:index,5], label = "distal3")

        plt.legend(bbox_to_anchor=(0, 1), loc='lower left', ncol = 3)
        plt.show()
        
    def datasetEntryPrepareAndSave(self, tasks,iteration):
        #check if the run was valid, eg. no grasp failure caused by 
        graspIndex = np.where(self.failFlag==1)
        collisionIndex = np.where(self.unwantedCollisionFlag==1)
        #print(graspIndex[0])
        #print(collisionIndex[0])
        if len(np.where(self.failFlag == 1)[0]) == 0 or len(np.where(self.unwantedCollisionFlag==1)[0]) == 0:
            ifValid = 1
        elif graspIndex[0][0]>collisionIndex[0][0]:
            ifValid = 0
        else:
            ifValid = 1
        #print(graspIndex)
        #line 1 - tactile info, line 2 - flags, line 3 - payload physics, line 4 - tasks, 
        dataset = [self.proximal1[:,:,2], self.proximal2[:,:,2], self.proximal3[:,:,2], self.distal1[:,:,2], self.distal2[:,:,2], self.distal3[:,:,2],
                   self.unwantedCollisionFlag, self.failFlag,
                   self.payloadOrientation, self.payloadVelocity, self.payloadAcceleration,
                   tasks, ifValid
                   ]
        #print(self.proximal1)
        #print()
        print(dataset[0])
        entryName = "TestEntry" + str(iteration) + ".npy"
        fileName = "Dataset/" + entryName
        np.save(fileName, dataset)
        


        
        
        
