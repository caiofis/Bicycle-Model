Tutorials
===========
This page shows how to implements the code in various ways.

Random Path Simulator
---------------------
This example show how to use the basic class **Bicycle**.

Its initialize a model with one meter between the wheels and max steer angle of
50º. The **sim_RandomPath** method simulate the model running at a constant
speed and a random steer angle for a number of steps, in the example 1m per step
for 1000 steps. ::

  import bicycle                          #import the model
  import matplotlib.pyplot as plt         #import matplotlib

  robot = bicycle.Bicycle(1,50)           #create a robot
  robot.sim_RandomPath(1,1000)            #run in a random path

  robot.show()                            #show the paths
  plt.show()                              #hold the plot

This code will result in a random trajectory of the model plot as a map-like
image, its a simple way to get lots of studies cases. The image below show a
example of plot from the code, you should get a different result as the code
uses a random function.

.. figure::  images/random.png
 :align:   center
 
 Random path

Odometry Simulator
------------------
The **vehicle class** inherits the features of the bicycle and add some sensors,
making possible keep a history of the speeds and the steer angles of the model
all through its path.

Real encoders is not perfect(it really away from it in fact), so the simulator
add a Gaussian noise to its reads, making it more close to the real world robots
, you should set the standard deviation of the noise. The steer angle is assume
as a truth information, so no noise is add to it.

This example create a rectangular path and run it on a **vehicle** with a noisy
encoder, then show the path using directly the sensors data, with no filter, as
expected this result in a different path by the propagation of the error in the
measurements. ::

  import vehicle                          #import the vehicle model
  import matplotlib.pyplot as plt         #import matplotlib

  robot = vehicle.Vehicle(1,50)           #create a robot
  robot.setOdometry(True)                 #set the odometer on
  robot.setOdometryVariance(0.4)          #configure its deviantion to 0.4
  speed,angle = [],[]                     #initialize the lists

  for a in xrange(4):                     #create a retangular path
      for i in xrange(400):
        angle.append(0)
      for i in xrange(107):
        angle.append(40)
  for i in xrange(len(angle)):        #set the speed to a constant along the path
    speed.append(1)

  robot.sim_Path(speed,angle)             #run in a rectangular path
  speed , angle =  robot.readOdometry()   #reads the sensors
  robot2 = vehicle.Vehicle()              #create a second model
  robot2.sim_Path(speed,angle)            #run it in the path read by odometry

  #show the paths
  robot.show("Real")
  robot2.show("Odometry")
  plt.show()

.. figure::  images/odometry.png
 :align:   center

 Real path and odometry based path

PID Control Simulator
---------------------
