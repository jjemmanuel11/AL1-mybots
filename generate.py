import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    x=1.5
    y=1.5
    z=.5

    length= 1
    width=1
    height=1

    pyrosim.Send_Cube(name="Box", pos=[x ,y ,z] , size=[length,width,height])


    pyrosim.End()

def Create_Robot():
    x=0
    y=0
    z=0.5

    length= 1
    width=1
    height=1
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0.5 ,0 ,0.5] , size=[length,width,height])

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
    type = "revolute", position = [1,0,0])

    pyrosim.Send_Cube(name="BackLeg", pos=[0.5 ,0 ,-0.5] , size=[1,1,1])

    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "FrontLeg" , child = "Torso" , 
    type = "revolute", position = [1,0,1])

    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5 ,0 ,0.5] , size=[1,1,1])

    pyrosim.End()
    
Create_World()
Create_Robot()

