import vehicle
import matplotlib.pyplot as plt

""" Simulate a robot in random path then draw the path read direct from the
    odometry with no filter"""

robot = vehicle.Vehicle(1,50)           #create a robot
robot.setOdometry(True)                 #configure its odometer
robot.setOdometryVariance(0.4)
robot.sim_RandomPath(1,1000)            #run in a random path
speed , angle =  robot.Odometry()       #reads the sensors
robot2 = vehicle.Vehicle()              #create a second model
robot2.sim_Path(speed,angle)            #run it in the path read by odometry

#show the paths
robot.show("Real")
robot2.show("Odometry")
plt.show()
