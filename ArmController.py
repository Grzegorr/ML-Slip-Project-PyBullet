#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class ArmController:
    lowerlimits = [-2.9671,-1.7628,-2.8973,-3.0718,-2.8973,-0.0175,-2.8973,100,100,100,100,100,100,100,100]
    upperlimits = [2.9671,1.7628,2.8973,0,2.8973,3.7525,2.8973,-110,-110,-110,-110,-110,-110,-110,-110]
    ranges = np.subtract(upperlimits, lowerlimits)
    restPoses = [0,0,0,0,0,0,0.8,0,0,0,0,0,0,0,0]
    
    
    
    def __init__(self, bulletClient, ArmId):
        print("Arm Controller initialized")
        print(self.ranges)
        self.client = bulletClient
        self.ArmId = ArmId
        
    def frankaJointsLock(self):
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=1, controlMode=self.client.VELOCITY_CONTROL, force = 10000)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=2, controlMode=self.client.VELOCITY_CONTROL, force = 10000)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=3, controlMode=self.client.VELOCITY_CONTROL, force = 10000)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=4, controlMode=self.client.VELOCITY_CONTROL, force = 10000)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=5, controlMode=self.client.VELOCITY_CONTROL, force = 10000)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=6, controlMode=self.client.VELOCITY_CONTROL, force = 10000)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=7, controlMode=self.client.VELOCITY_CONTROL, force = 10000)
        
    def frankaJointsUnlock(self):
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=1, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=2, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=3, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=4, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=5, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=6, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=7, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        
    def IKiteration(self, position, Orientation,simStep, startStep, stopStep):
        if simStep > startStep and simStep < stopStep:
            jointPoses = self.client.calculateInverseKinematics(self.ArmId, 60, position, targetOrientation = Orientation)
            for i in range(len(jointPoses)):
                self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=i, controlMode=self.client.POSITION_CONTROL, targetPosition=jointPoses[i], targetVelocity=0, force=5000, maxVelocity = 1)
            
    def IKiterationAuto(self, position, Orientation,simStep, startStep, stopStep, targetVelocity, maxVel, Vgain, Pgain):
         if simStep > startStep and simStep < stopStep:
            jointPoses = self.client.calculateInverseKinematics(self.ArmId, 60, position, targetOrientation = Orientation)
            for i in range(len(jointPoses)):
                self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=i, controlMode=self.client.POSITION_CONTROL, targetPosition=jointPoses[i], targetVelocity=targetVelocity, force=5000, maxVelocity = maxVel, velocityGain = Vgain, positionGain = Pgain )
      
    
    def IKiterationAuto2(self, position, Orientation,simStep, startStep, stopStep, targetVelocity, maxVel, Vgain, Pgain):
         if simStep > startStep and simStep < stopStep:
            jointPoses = self.client.calculateInverseKinematics(self.ArmId, 60, position, targetOrientation = Orientation)
            for i in range(len(jointPoses)):
                self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=i, controlMode=self.client.POSITION_CONTROL, targetPosition=jointPoses[i], targetVelocity=targetVelocity, force=5000, maxVelocity = maxVel, velocityGain = Vgain, positionGain = Pgain )
    
        
    def runSeriesOfIKTasks(self,i,tasks):
        #print("Run series of tasks")
    #tasks[x]= [simStepStart, positionEndEffector, orientationEndEffector, targetVel,maxVel, Vgain, Pgain]
        if i == 0:
            self.taskCounter = 0
        #print(self.taskCounter)
        #print(tasks[self.taskCounter][0])
        if i > tasks[self.taskCounter][0]: #is it after the start step of current task
            if len(tasks)-1 > self.taskCounter: 
                if i == tasks[self.taskCounter + 1][0]:
                    self.taskCounter = self.taskCounter + 1
            #print("before IK")
            if i % 10 == 0:
                jointPoses = self.client.calculateInverseKinematics(self.ArmId, 60, tasks[self.taskCounter][1], targetOrientation = tasks[self.taskCounter][2])#, lowerLimits = self.lowerlimits, upperLimits = self.upperlimits, jointRanges = self.ranges, restPoses = self.restPoses)
            #print("after IK")
            #print(jointPoses)
            #print(len(jointPoses))
                for j in range(7):
                    self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=j, controlMode=self.client.POSITION_CONTROL, targetPosition=jointPoses[j], targetVelocity=tasks[self.taskCounter][3], force=5000, maxVelocity = tasks[self.taskCounter][4], velocityGain = tasks[self.taskCounter][5], positionGain = tasks[self.taskCounter][6] )
            
            
    def accurateCalculateInverseKinematics(kukaId, endEffectorId, targetPos, threshold, maxIter):
        closeEnough = False
        iter = 0
        dist2 = 1e30
        while (not closeEnough and iter < maxIter):
            jointPoses = p.calculateInverseKinematics(kukaId, kukaEndEffectorIndex, targetPos)
            for i in range(numJoints):
                p.resetJointState(kukaId, i, jointPoses[i])
                ls = p.getLinkState(kukaId, kukaEndEffectorIndex)
                newPos = ls[4]
                diff = [targetPos[0] - newPos[0], targetPos[1] - newPos[1], targetPos[2] - newPos[2]]
                dist2 = (diff[0] * diff[0] + diff[1] * diff[1] + diff[2] * diff[2])
                closeEnough = (dist2 < threshold)
            iter = iter + 1
            
    def rollLastJoint(self, vel):
        #self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=7, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
        self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=6, controlMode=self.client.POSITION_CONTROL, targetPosition=0, targetVelocity=0, force=0)
        self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=6, controlMode=self.client.VELOCITY_CONTROL, targetVelocity = vel, force = 10, velocityGain = 0.5)
        #self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=5, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
        #self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=4, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
        #self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=3, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
        #self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=2, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
        #self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=1, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
        
    
    #Tkes 6000 simulation steps
    def GrabbingSequence(self,i, startStep, G):
        i = i - startStep
        self.IKiteration([0.5,0.3,0.5], self.client.getQuaternionFromEuler([1.57,0,0]), i, 0,500)
        self.IKiteration([0.7,0.3,0.3], self.client.getQuaternionFromEuler([1.57,0,0]), i, 500,1000)
        self.IKiteration([0.5,0.2,0.3], self.client.getQuaternionFromEuler([1.57,0,0]), i, 1000,1500)
        self.IKiteration([0.5,0.1,0.15], self.client.getQuaternionFromEuler([1.57,0,0]), i, 1500,2000)
        self.IKiteration([0.5,0,0.15], self.client.getQuaternionFromEuler([1.57,0,0]), i, 2000,2500)
        if i == 2500:
            self.frankaJointsLock()
        if i > 2500 and i < 6000:
            G.closeHandAdvanced()
            G.spreadFingers(0)
        if i > 6050:
            G.closeHandTorques()
        self.IKiteration([0.5,0,0.5], self.client.getQuaternionFromEuler([1.57,0,0]), i, 6100,6400)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    