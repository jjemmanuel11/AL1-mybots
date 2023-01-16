import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time 
import numpy 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(500)



for i in range(500):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1/50)
   
print(backLegSensorValues)
numpy.save("data/backLegSensorValues", backLegSensorValues)   
p.disconnect()




