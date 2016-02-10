import math
import random
import matplotlib.pyplot as plt
import bicycle

class Vehicle(bicycle.Bicycle):
    """The Vehicle is based on the Bicycle class, the diferece is the it has
        sensors em methods for odometry"""
    def __init__(self,L,alpha_max):
        bicycle.Bicycle.__init__(self,L,alpha_max)
        self.odoState = False   #turn of odometry
        self.odoVariance = 0    #set the standard deviantion of the odometry to
                                # zero
        self.sensors = [[],[]]  # inicialize a list of the sensors,
                                # sensors[0] = encoder
                                # sensors[1] = steer angle
    def setOdometry(self,state):
    # turn on or off the odometry
        self.odoState = state
    def setOdometryVariance(self, variance):
    # Set the valor of the standard deviantion of the odometry
        self.odoVariance = variance
    def readSensors(self,v,alpha):
    # append to the list the encoder read
        v += random.gauss(0,self.odoVariance) # append the noise to the odometer
        self.sensors[0].append(v)
        self.sensors[1].append(alpha)
    def Odometry(self):                      # return the list of sensors reads
        return self.sensors
    def run(self, v, alpha):
    # Atualize the run method to read the sensors too
        bicycle.Bicycle.run(self,v,alpha)
        self.readSensors(v,alpha)
    def clear(self):
        bicycle.Bicycle.clear()
        self.sensors = [[],[]]  # clear list of the sensors
