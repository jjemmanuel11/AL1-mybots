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
        self.sensors = []
        self.count = 0

    def Start_Simulation(self, directOrGui):
        pyrosim.Start_SDF("world.sdf")
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " 2&>1")


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
        z_pos = 2

        x_size = 1
        y_size = 1
        z_size = 1

        #head - 'link0'
        pyrosim.Send_Cube(name= "link0", pos=[x_pos, y_pos, z_pos] , size=[x_size,y_size,z_size])
        pyrosim.Send_Joint(name = "link0_link1" , parent= "link0" , child = "link1" , type = "revolute", position = [x_pos,y_pos + y_size/2,z_pos], jointAxis="1 0 0")

        for i in range(1,num_links):
            pz_size = z_size

            x_size = random.randint(1,4)
            y_size = random.randint(1,4)
            z_size = random.randint(1,4)


            pyrosim.Send_Cube(name= "link" + str(i), pos=[x_pos, y_size/2, pz_size/2] , size=[x_size,y_size,z_size])

            if i + 1 >= num_links:
                pass
            else:
                pyrosim.Send_Joint(name = "link" + str(i) + "_" + "link" + str(i+1) , parent= "link" + str(i) , child = "link" + str(i+1) , type = "revolute", position = [x_pos,y_size,z_pos], jointAxis="1 0 0")
                print("num_links:",num_links)
    
        self.sensors = sensors
        
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        sensor_count = 0
        for k in self.sensors:
            if self.sensors[k] == 1:
                sensor_count += 1
        
        print("sensor count:", sensor_count)


        for i in range(len(self.sensors)):
            if(self.sensors[i] == 1):
                pyrosim.Send_Sensor_Neuron(name = i , linkName = "link" + str(i))
                print('sending sensor for ', i)
            if(i != len(self.sensors) - 1):
                pyrosim.Send_Motor_Neuron(name = i + 100, jointName = "link" + str(i) + "_" + "link" + str(i+1))
       
        for i in range(len(self.sensors)):
            if(self.sensors[i] == 1):
                for j in range(len(self.sensors) - 1):
                    pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j + 10, weight=1)


        


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

