###########
# IMPORTS #
###########

import os
import sys


#############
# FUNCTIONS #
#############

def spawn_files():
    file = open("data/total.csv", "w+")
    file.write(",".join(["scale", "throughput", "load", "collision", "lost"]))
    file.write("\n")
    file.close()

    file = open("data/nodes.csv", "w+")
    file.write(",".join(["node", "scale", "throughput", "load", "collision", "lost"]))
    file.write("\n")
    file.close()

def simulate(minVal, maxVal, step):
    for val in range(minVal, maxVal, step):
        scale = val/10000
        for seed in range(100):
            os.system("python iris/iris.py -q -s 1000 -f data -r "+str(seed)+" "+str(scale))
    print("[ STEP ]")


########
# MAIN #
########

if sys.version_info >= (3, 0):
    spawn_files()
    simulate(30, 72, 3)
    simulate(76, 139, 7)
    simulate(140, 470, 30)
    simulate(500, 1100, 100)
else:
    print("[ FAIL ] Python 3.x required")
