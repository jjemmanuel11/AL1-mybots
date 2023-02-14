import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(9, 8) * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGui):
        pyrosim.Start_SDF("world.sdf")
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " 2&>1 &")


    def Wait_For_Simulation_To_End(self):
        fitnessString = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessString):
            time.sleep(0.01)

        f = open(fitnessString, "r")
        self.fitness = float(f.read())
        f.close()

        os.system("rm " + fitnessString)

    
        


    def Create_World(self):
        pyrosim.Send_Cube(name="Box", pos=[-2,-2,.5] , size=[1,1,1])        
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        #randomize how many links there will be within a certain range 
        num_links = random.randint(4,10)
        #keep track of which links will have sensors or not --> to change colors
        sensors = []
        for i in range(num_links):
            sensors.append(random.randint(0,1))

        for i in range(num_links):
            if sensors[i] == 1:
                #green
                color_name = "Green"
                rgb_color = (1,255,10)
            else:
                #blue
                color_name = "Blue"
                rgb_color = (1,255,231)
        

        #randomize sizes of links 
        x_pos = 0
        y_pos = 0
        z_pos = 2.5

        x_size = 1
        y_size = 1
        z_size = 1

        #head - 'link0'
        pyrosim.Send_Cube(name= "link0", pos=[x_pos, y_pos, z_pos] , size=[x_size,y_size,z_size])
        pyrosim.Send_Joint(name = "link0" , parent= "link0" , child = "link1" , type = "revolute", position = [x_pos,y_pos + y_size/2,z_pos], jointAxis="1 0 0")

        for i in range(1,num_links):
            
            x_size = random.randint(1,5)
            y_size = random.randint(1,5)
            z_size = random.randint(1,5)


            pyrosim.Send_Cube(name= "link" + str(i), pos=[x_pos, y_size/2, z_pos] , size=[x_size,y_size,z_size])
            if i <= num_links:
                pyrosim.Send_Joint(name = "link" + str(i) + "_" + "link" + str(i+1) , parent= "link" + str(i) , child = "link" + str(i+1) , type = "revolute", position = [x_pos,y_size,z_pos], jointAxis="1 0 0")

        self.sensors = sensors


        # pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1] , size=[3,1,0.75])

        # #FRONT LEG
        # pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0.5,1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0.5, 0] , size=[.2,1,.2])

        # pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0.5, 0, -.5] , size=[.2,.2,1])

        # #BACK LEG
        # pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5, -.5, 1], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="BackLeg", pos=[0.5, -0.5, 0] , size=[.2,1,.2])

        # pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.5,-1,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5] , size=[.2,.2,1])

        # #LEFT LEG
        # pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0.5,1], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, .5, 0] , size=[.2,1,.2])

        # pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [0,1,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[-0.5, 0, -.5] , size=[.2,.2,1])

        # #RIGHT LEG
        # pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [-0.5, -0.5, 1], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="RightLeg", pos=[-.5, -0.5, 0] , size=[.2,1,.2])

        # pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [-.5, -1,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5] , size=[.2,.2,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        #make sensors for the assigned links
        for i in range(len(self.sensors)):
            if(self.sensors[i] == 1):
                pyrosim.Send_Sensor_Neuron(name = i , linkName = "link" + str(i))
                print('sending sensor for ', i)
            if(i != len(self.sensors) - 1):
                pyrosim.Send_Motor_Neuron(name = i + 100, jointName = "link" + str(i) + "_" + "link" + str(i+1))
        #attach a motor to every joint
    
        #create a syanpse between every sensor neuron and every motor neuron
        for i in range(len(self.sensors)):
            if(self.sensors[i] == 1):
                for j in range(len(self.sensors) - 1):
                    pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j + 100, weight=1)

        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")

        # pyrosim.Send_Sensor_Neuron(name = 5, linkName="FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6, linkName="BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 7, linkName="LeftLowerLeg")
        # # pyrosim.Send_Sensor_Neuron(name = 8, linkName="RightLowerLeg")

        # pyrosim.Send_Motor_Neuron(name = 9, jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron(name = 10, jointName = 'Torso_FrontLeg')
        # pyrosim.Send_Motor_Neuron(name = 11, jointName="Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron(name = 12, jointName="Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron(name = 13, jointName="FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron(name = 14, jointName="BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron(name = 15, jointName="LeftLeg_LeftLowerLeg")
        # # pyrosim.Send_Motor_Neuron(name = 16, jointName="RightLeg_RightLowerLeg")


        #UNCOMMENT THIS LATER!!!
        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])


        pyrosim.End()
    def Mutate(self):
        randomRow = random.randint(0, 2)
     
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id