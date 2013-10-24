## Joshua Winchester jwinchester6@gatech.edu
## Sahithi Solipuram ssolipuram3@gatech.edu
## We worked on this assignament alone and using only course materials.

from Myro import *
init("sim")

def roboScript(filename):
    myFile = open(filename, "r")
    read = True
    while read == True:
        line = myFile.readline()
        if line == "":
            break
        actions = line.split()
        
        if actions[0] == "fw":
            forward(float(actions[1]),float(actions[2]))
        elif actions[0] == "bw":
            backward(float(actions[1]),float(actions[2]))
        elif actions[0] == "tr":
            turnRight(float(actions[1]),float(actions[2]))
        elif actions[0] == "tl":
            turnLeft(float(actions[1]),float(actions[2]))
        elif actions[0] == "bp":
            beep(float(actions[2]),float(actions[1]))
    myFile.close()