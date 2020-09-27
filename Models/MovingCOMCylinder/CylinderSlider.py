#Simple simulation to test the cylinder on the go
#loads model from the same directory the script is located

import time
import pybullet as p
import pybullet_data

#Connet to the API
physicsClient = p.connect(p.GUI)

#Path to defaultyly downloaded data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Setting the gravity
p.setGravity(0,0,-10)

#Load-in a plane
planeId = p.loadURDF("plane.urdf")

startPos = [0,0,3]
startOrientation = p.getQuaternionFromEuler([0,0,0])
Cylinder = p.loadURDF("COMcylinderSlider.urdf",startPos, startOrientation)

n = p.getNumJoints(Cylinder)
for i in range(n):
    print(p.getJointInfo(Cylinder,i))

p.setJointMotorControl2(bodyUniqueId=Cylinder, jointIndex=91, controlMode=p.VELOCITY_CONTROL, force = 0)




for i in range (0,20000):
    p.stepSimulation()
    time.sleep(1./240.)