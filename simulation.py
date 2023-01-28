from world import WORLD
from robot import ROBOT 
import pybullet as p
import constants as c
import pybullet_data
import time




class SIMULATION:
    def __init__(self, directOrGui):
        if directOrGui == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
        self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
       


    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            # time.sleep(1/500)
    
    def Get_Fitness(self):
        self.robot.Get_Fitnness()
            
    
    def __del__(self):
        p.disconnect()
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
   


        

        
        