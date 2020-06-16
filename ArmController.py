#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ArmController:
    
    def __init__(self, bulletClient, ArmId):
        print("Arm Controller initialized")
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
            jointPoses = self.client.calculateInverseKinematics(self.ArmId, 61, position, targetOrientation = Orientation)
            for i in range(len(jointPoses)):
                self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=i, controlMode=self.client.POSITION_CONTROL, targetPosition=jointPoses[i], targetVelocity=0, force=5000, maxVelocity = 1)
            
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
            
    def rollLastJoint(self, pos):
        #self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=7, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
        self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=6, controlMode=self.client.POSITION_CONTROL, targetPosition=pos, targetVelocity=0, force=5000, maxVelocity = 1)
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
        self.IKiteration([0.5,0.1,0.3], self.client.getQuaternionFromEuler([1.57,0,0]), i, 1500,2000)
        self.IKiteration([0.5,0,0.3], self.client.getQuaternionFromEuler([1.57,0,0]), i, 2000,2500)
        if i == 2500:
            self.frankaJointsLock()
        if i > 2500 and i < 6000:
            G.closeHandAdvanced()
            G.spreadFingers(0)
        if i > 6050:
            G.closeHandTorques()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    