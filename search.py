import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER 

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

#
# add for loop
# for i in range(1):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")
