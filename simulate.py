import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time 
import numpy 
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(500)
frontLegSensorValues = numpy.zeros(500)



for i in range(500):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = 'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = random.random(),
    maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = 'Torso_FrontLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = random.random(),
    maxForce = 500)

    time.sleep(1/50)
   
print(backLegSensorValues)
numpy.save("data/backLegSensorValues", backLegSensorValues) 
numpy.save("data/frontLegSensorValues", frontLegSensorValues)   
p.disconnect()




