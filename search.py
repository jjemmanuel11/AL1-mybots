import os
from hillclimber import HILL_CLIMBER 

hc = HILL_CLIMBER()

hc.Evolve()
hc.Show_Best()


# add for loop
# for i in range(1):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")
