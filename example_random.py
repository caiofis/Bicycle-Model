import bicycle
import matplotlib.pyplot as plt

""" Simulate a robot in random path then draw the path read direct from the
    odometry with no filter"""

robot = bicycle.Bicycle(1,50)           #create a robot
robot.sim_RandomPath(1,1000)            #run in a random path

#show the paths
robot.show()
plt.show()
