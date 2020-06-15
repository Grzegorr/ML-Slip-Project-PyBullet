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
                self.client.setJointMotorControl2(bodyIndex=self.ArmId, jointIndex=i, controlMode=self.client.POSITION_CONTROL, targetPosition=jointPoses[i], targetVelocity=0, force=5000, positionGain=0.5, velocityGain=0.6)
            
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
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    