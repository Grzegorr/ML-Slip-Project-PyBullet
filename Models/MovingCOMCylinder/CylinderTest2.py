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

startPos = [0,0,30]
startOrientation = p.getQuaternionFromEuler([0,0,0])
TheArm = p.loadURDF("COMcylinder.urdf",startPos, startOrientation)

for x in range(-1,2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            x = x/10.0
            y = y / 10.0
            z = z / 10.0
            startPos = [0+x,0+y,30.25+z]
            startOrientation = p.getQuaternionFromEuler([0,0,0])
            TheArm = p.loadURDF("box2.urdf",startPos, startOrientation)


for i in range (0,20000):
    p.stepSimulation()
    time.sleep(1./240.)