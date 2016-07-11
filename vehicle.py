import math
import random
import matplotlib.pyplot as plt
import bicycle

class Vehicle(bicycle.Bicycle):
    """The Vehicle is based on the Bicycle class, the diferece is the it has
        sensors em methods for odometry"""
    def __init__(self, L = 1 ,alpha_max = 90):
        bicycle.Bicycle.__init__(self,L,alpha_max)
        self.odoState = False   #turn of odometry
        self.odoVariance = [0,0]    #set the standard deviantion of the odometry to
                                # zero
        self.sensors = [[],[]]  # inicialize a list of the sensors reads,
                                # sensors[0] = encoder
                                # sensors[1] = steer angle
    def setOdometry(self,state):
        """Turn on or off the odometry, the odometry reads the speed of the model
        and adds a gaussian noise to it, the standard deviantion of this noise
        must be set"""
        self.odoState = state
    def setOdometryVariance(self, variance):
        """Set the valor of the standard deviantion of the odometry
            It must be a list of two values [encoder,steer]"""
        self.odoVariance = variance
    def readSensors(self,v,alpha):
        """Append to the list the reads of the sensors (encoder and steer angle
    measurement)"""
        v += random.gauss(0,self.odoVariance[0]) # append the noise to the odometer
        alpha += random.gauss(0,self.odoVariance[1])
        self.sensors[0].append(v)
        self.sensors[1].append(alpha)
    def Odometry(self,v,alpha):
        """Make the read of the sensors if the odometry is set"""
        if(self.odoState):
            self.readSensors(v,alpha)
    def readOdometry(self):
        """Return the list of sensors reads of the encoder and the steer angles"""
        return self.sensors[0],self.sensors[1]
    def run(self, v, alpha):
        """Calculate the next pose of the model and read the sensors"""
        bicycle.Bicycle.run(self,v,alpha)
        self.Odometry(v,alpha)
    def clear(self):
        """Clear both the poses of the model and the sensors reads"""
        self.poses = [[],[],[]]
        self.sensors = [[],[]]  # clear list of the sensors
