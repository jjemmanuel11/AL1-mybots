
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from motor import MOTOR
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_to_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")

    
    def Prepare_to_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Sense(self, time):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(time)

    
    def Act(self, time):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                print(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                print(jointName)
                print(desiredAngle)

        # for motor in self.motors:
        #     self.motors[motor].Set_Value(self.robotId, time)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
        

            

        