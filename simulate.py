from simulation import SIMULATION
import sys  

directorOrGUI = sys.argv[1]
simulation = SIMULATION(directorOrGUI)
simulation.Run()
simulation.Get_Fitness()




# import pybullet as p
# import pyrosim.pyrosim as pyrosim
# import pybullet_data
# import time 
# import numpy 
# import random
# import constants as c

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())


# p.setGravity(0,0,-9.8)
# p.loadSDF("world.sdf")
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# pyrosim.Prepare_To_Simulate(robotId)
# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)



# SinValue = numpy.linspace(0, 2*numpy.pi, 1000)
# BackSin = numpy.linspace(0, 2*numpy.pi, 1000)
# FrontSin = numpy.linspace(0, 2*numpy.pi, 1000)

# for j in range(1000):
#     BackSin[j]= c.amplitude_back * numpy.sin(c.frequency_back * SinValue[j] + c.phaseOffset_back)
#     FrontSin[j]= c.amplitude_front * numpy.sin(c.frequency_front * SinValue[j] + c.phaseOffset_front)
# for i in range(500):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = 'Torso_BackLeg',
#     controlMode = p.POSITION_CONTROL,
#     targetPosition = BackSin[i],
#     maxForce = 200)

#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = 'Torso_FrontLeg',
#     controlMode = p.POSITION_CONTROL,
#     targetPosition = FrontSin[i],
#     maxForce = 500)

#     time.sleep(1/120)
   
# print(backLegSensorValues)

# numpy.save("data/backLegSensorValues", backLegSensorValues) 
# numpy.save("data/frontLegSensorValues", frontLegSensorValues)   
# p.disconnect()




