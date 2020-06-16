#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


class Statistics:
    
    def __init__(self):
        print("Using Statistics Class")
        self.proximal1 = np.zeros((10000,5,6))
        self.proximal2 = np.zeros((10000,5,6))
        self.proximal3 = np.zeros((10000,5,6))
        self.distal1 = np.zeros((10000,4,6))
        self.distal2 = np.zeros((10000,4,6))
        self.distal3 = np.zeros((10000,4,6))
        self.handForces = np.zeros((10000,6))
        
    def readWrenches(self, simStep, proximal1, proximal2, proximal3, distal1, distal2, distal3):
        index = int(simStep/24)
        self.proximal1[index] = proximal1
        self.proximal2[index] = proximal2
        self.proximal3[index] = proximal3
        self.distal1[index] = distal1
        self.distal2[index] = distal2
        self.distal3[index] = distal3
        
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
        
        
        
