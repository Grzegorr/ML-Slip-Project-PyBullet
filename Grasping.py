#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Grasping:
    lowerlimits = [-2.9671,-1.7628,-2.8973,-3.0718,-2.8973,-0.0175,-2.8973,0,0,0,0,0,0,0,0]
    upperlimits = [2.9671,1.7628,2.8973,-0.0698,2.8973,3.7525,2.8973,0,0,0,0,0,0,0,0]
    
    def __init__(self, bulletClient, ArmId):
        print("Using Grasp Package")
        self.client = bulletClient
        self.ArmId = ArmId
        self.RadToDeg = 3.14/180.0
        #TURN ON FORCE AND TORQUE SENSING IN THE JOINTS
        self.turnSensorsOn()
        
    def returnLimits(self):
        return self.lowerlimits, self.upperlimits
    
    def closeHandTorques(self):
        print("Closing Hand")
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=11, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=11, controlMode=self.client.TORQUE_CONTROL, force = 1)  
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=28, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=28, controlMode=self.client.TORQUE_CONTROL, force = 1)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=44, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=44, controlMode=self.client.TORQUE_CONTROL, force = 1)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=13, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=13, controlMode=self.client.TORQUE_CONTROL, force = 0.2)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=30, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=30, controlMode=self.client.TORQUE_CONTROL, force = 0.2)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=46, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=46, controlMode=self.client.TORQUE_CONTROL, force = 0.2)
    
    def openHandTorques(self):
        print("Opening Hand")
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=11, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=11, controlMode=self.client.TORQUE_CONTROL, force = -1)  
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=28, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=28, controlMode=self.client.TORQUE_CONTROL, force = -1)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=44, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=44, controlMode=self.client.TORQUE_CONTROL, force = -1)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=13, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=13, controlMode=self.client.TORQUE_CONTROL, force = -0.2)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=30, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=30, controlMode=self.client.TORQUE_CONTROL, force = -0.2)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=46, controlMode=self.client.VELOCITY_CONTROL, force = 0)
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=46, controlMode=self.client.TORQUE_CONTROL, force = -0.2)
    
    def spreadFingers(self, targetAng):
        targetAng = targetAng * self.RadToDeg
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=10, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng, maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=27, controlMode=self.client.POSITION_CONTROL, targetPosition = -targetAng, maxVelocity = 1) 
        
    def stiffFingerClosePosition(self,targetAng):
        targetAng = targetAng * self.RadToDeg
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=11, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=28, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=44, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=13, controlMode=self.client.POSITION_CONTROL, targetPosition = 0,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=30, controlMode=self.client.POSITION_CONTROL, targetPosition = 0,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=46, controlMode=self.client.POSITION_CONTROL, targetPosition = 0,maxVelocity = 1)    
    def spreadFingersOld(self, targetAng):
        targetAng = targetAng * self.RadToDeg
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=10, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng, maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=16, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng, maxVelocity = 1) 
        
    def stiffFingerClosePositionOld(self,targetAng):
        targetAng = targetAng * self.RadToDeg
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=11, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=17, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        self.client.setJointMotorControl2(bodyUniqueId=self.ArmId, jointIndex=22, controlMode=self.client.POSITION_CONTROL, targetPosition = targetAng,maxVelocity = 1) 
        
    def turnSensorsOn(self):
        for sensor_joint in [16,17,18,19,22,23,24,25,26,
                             33,34,35,36,39,40,41,42,43,
                             49,50,51,52,55,56,57,58,59]:
            self.client.enableJointForceTorqueSensor(bodyUniqueId=self.ArmId, jointIndex=sensor_joint)
            
    #For Each sensing joint we get [Fx,Fy,Fz,Mx,My,Mz]        
    def readTactile(self):
        proximal1 = [0,0,0,0,0]
        distal1 = [0,0,0,0]
        proximal2 = [0,0,0,0,0]
        distal2 = [0,0,0,0]
        proximal3 = [0,0,0,0,0]
        distal3 = [0,0,0,0]
        
        entry = 2 
        #Proximal - finger1
        for sensor_joint in [22,23,24,25,26]:
            proximal1[sensor_joint-22] = self.client.getJointState(self.ArmId,sensor_joint)[2][entry]
        #Distal - finger1
        for sensor_joint in [16,17,18,19]:
            distal1[sensor_joint-16] = self.client.getJointState(self.ArmId,sensor_joint)[2][entry]   
        #Proximal - finger2
        for sensor_joint in [39,40,41,42,43]:
            proximal2[sensor_joint-39] = self.client.getJointState(self.ArmId,sensor_joint)[2][entry]
        #Distal - finger2
        for sensor_joint in [33,34,35,36]:
            distal2[sensor_joint-33] = self.client.getJointState(self.ArmId,sensor_joint)[2][entry]
        #Proximal - finger3
        for sensor_joint in [55,56,57,58,59]:
            proximal3[sensor_joint-55] = self.client.getJointState(self.ArmId,sensor_joint)[2][entry]
        #Distal - finger3
        for sensor_joint in [49,50,51,52]:
            distal3[sensor_joint-49] = self.client.getJointState(self.ArmId,sensor_joint)[2][entry]
            
        #print(proximal1)
        #print(distal1[0])
        #print(distal1[0][0])
        #print(format(distal1[0][0], '.4f'))
        #print()
        #print(format(distal1[0], '.4f') + " , " + format(distal1[1], '.4f') + " , " + format(distal1[2], '.4f') + " , " + format(distal1[3], '.4f'))
        #print(format(proximal1[0], '.4f') + " , " + format(proximal1[1], '.4f') + " , " + format(proximal1[2], '.4f') + " , " + format(proximal1[3], '.4f')+ " , " + format(proximal1[4], '.4f'))
        
        return proximal1, proximal2, proximal3, distal1, distal2, distal3
        
        
        
        
        
        
        
        
        
        
        
        