from colorclass import Windows
import re
import traceback

Windows.enable()

# distributions
#

PACKET_SIZE_DISTRIBUTION = ""
INTERARRIVAL_TIME_DISTRIBUTION = ""
UNIFORM_MIN = 1
UNIFORM_MAX = 1
GAMMA_SHAPE = 1
GAMMA_SCALE = 1
SEED = None

# net
#

BOUNDS = 0.25
BUFFER = 0
SPEED = 1*1000*1000 # 1 MB or 8 Mb
NODES = []

POINTS = []
packet_size_re = "\t(\w+)\(a=(\d+), b=(\d+).*"
arrival_time_re = "\t(\w+)\(shape=([\d\?\.]+), scale=([\d\?\.]+).*"
buffer_size_re = "Node buffer size: (\d+)"
points_re = "Node\d\(0\.(\d+), 0\.(\d+)\);"
try:
    for i, line in enumerate(open('./data/affabris.data')):
        size = re.search(packet_size_re, line)
        if(size):
            PACKET_SIZE_DISTRIBUTION = size.group(1)
            UNIFORM_MIN = int(size.group(2))
            UNIFORM_MAX = int(size.group(3))
        time = re.search(arrival_time_re, line)
        if(time):
            INTERARRIVAL_TIME_DISTRIBUTION = time.group(1)
            GAMMA_SHAPE = float(time.group(2)) if time.group(2) != "?" else "None"
            GAMMA_SCALE = float(time.group(3)) if time.group(3) != "?" else "None"
        buffer_size = re.search(buffer_size_re, line)
        if(buffer_size):
            BUFFER = int(buffer_size.group(1))
        node = re.search(points_re, line)
        if(node):
            POINTS.append((int(node.group(1))/1000, int(node.group(2))/1000))
except:
    traceback.print_exc()

# simulation
#

VERBOSE = None
QUIET = None
FOLDER = None
TIME = None
STEPS = None
PRECISION = "{:.8g}"
