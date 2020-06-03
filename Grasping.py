#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Grasping:
    
    def __init__(self, bulletClient, ArmId):
        print("Using Grasp Package")
        self.client = bulletClient
        self.ArmId = ArmId
        self.RadToDeg = 3.14/180.0
        #TURN ON FORCE AND TORQUE SENSING IN THE JOINTS
        self.turnSensorsOn()
        
    def spreadFingers(self, targetAng):
        targetAng = targetAng * self.RadToDeg
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=10, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng, maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=16, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng, maxVelocity = 1) 
        
    def stiffFingerClosePosition(self,targetAng):
        targetAng = targetAng * self.RadToDeg
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=11, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=17, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=22, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        
    def turnSensorsOn(self):
        for sensor_joint in [16,17,18,19,22,23,24,25,26,
                             33,34,35,36,39,40,41,42,43,
                             49,50,51,52,55,56,57,58,59]:
            self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=sensor_joint, controlMode=self.client.POSITION_CONTROL, targetPosition = 1, maxVelocity = 1)