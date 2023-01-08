import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])

x=0
for i in range(5):
    y=0
    for j in range(5):
        length=1
        width=1
        height=1
        z=0
        for k in range(0,10):
            pyrosim.Send_Cube(name="Box", pos=[x ,y ,z] , size=[length,width,height])
            z = z + height/2 + height *.9/2
            length = length*0.9
            width= width * 0.9
            height= height * 0.9
        y+=1
    x+=1
            
pyrosim.End()
