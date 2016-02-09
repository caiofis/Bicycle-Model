import math
import random
import matplotlib.pyplot as plt

class Bicycle(object):
    """docstring for """
    def __init__(self, L,alpha_max):
        # inicialize bicycle model
        self.L = L                      # L is the length between the wheels
        self.alpha_max = alpha_max      # alpha_max is the maximal angle of the
        self.x = 0                      # front axis
        self.y = 0                      # the inicial position of the model is
        self.theta = 0                  # (0,0,0) and the pose is (x,y,theta)
        self.poses = [[],[],[]]         # list od the poses of the model
    def clear(self):
        #clear the list of poses
        self.poses = [[],[],[]]
    def setPose(self,x,y,theta):
        #define a position
        self.x = x
        self.y = y
        self.theta = theta
    def Update(self,x,y,theta):
        #aplly the deltas to the pose and add pose to the list
        self.x += x
        self.y += y
        self.theta += theta
        self.poses[0].append(self.x)
        self.poses[1].append(self.y)
        self.poses[2].append(self.theta)
    def run(self,v,alpha):
        # Simulate a time step guetting the parameters
        # v is the velocity in this step and alpha is the angle of the front
        # axis in degrees
        delta_x = v*math.cos(math.radians(self.theta))
        delta_y = v*math.sin(math.radians(self.theta))
        delta_theta = (v/self.L)*math.tan(math.radians(alpha))
        self.Update(delta_x,delta_y,delta_theta)
    def show(self):
        # Plot the path of the model
        plt.plot(rob.poses[0],rob.poses[1])
        plt.show()
    def sim_RandomPath(self,v,steps):
        # Simulate a model with random alpha in it time steps
        # v is the contant speed of the model and steps is the num of
        # interations of the simulation
        for i in xrange(steps):
            alpha = random.gauss(0,self.alpha_max)
            self.run(v,alpha)
    def __str__(self):
        return str(self.poses)
