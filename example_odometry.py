import vehicle
import matplotlib.pyplot as plt

""" Simulate a robot in a rectangular path then draw the path read direct from the
    odometry with no filter"""

robot = vehicle.Vehicle(1,50)           #create a robot
robot.setOdometry(True)                 #configure its odometer
robot.setOdometryVariance(0.4)
speed,angle = [],[]
for a in xrange(4):                     #create a retangular path
    for i in xrange(400):
        angle.append(0)
    for i in xrange(107):
        angle.append(40)

for i in xrange(len(angle)):        #set the speed to a constant along the path
    speed.append(1)

robot.sim_Path(speed,angle)             #run in a rectangular path
speed , angle =  robot.Odometry()       #reads the sensors
robot2 = vehicle.Vehicle()              #create a second model
robot2.sim_Path(speed,angle)            #run it in the path read by odometry

#show the paths
robot.show("Real")
robot2.show("Odometry")
plt.show()
print robot.getPose()
