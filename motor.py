
import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_to_Act()

    def Prepare_to_Act(self):
        self.amplitude = c.amplitude_front
        self.frequency = c.frequency_front
        self.offset = c.phaseOffset_front
        self.motorValues = numpy.linspace(0, 2*numpy.pi, c.iterations)
        for x in range(c.iterations):
            self.motorValues[x] = self.amplitude * numpy.sin(self.frequency * self.motorValues[x] + self.offset)
    
    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex= robotId, jointName = self.jointName, controlMode= p.POSITION_CONTROL,
        targetPosition= desiredAngle, maxForce = c.maxForce)
    
    def Save_Values(self):
        numpy.save("data/" + self.jointName, self.motorValues)

    