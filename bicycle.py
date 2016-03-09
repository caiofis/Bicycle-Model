import math
import random
import matplotlib.pyplot as plt

class Bicycle(object):
    """Implementation of the famous bibycle "model"

    Inicialize the model, getting **L** = distance between the wheels and
    **alpha_max** = maximun steer angle

    **The distances must be ALLWAYS in meters**"""

    def __init__(self, L =1 ,alpha_max = 90):
        self.L = L                      # L is the length between the wheels
        self.alpha_max = alpha_max      # alpha_max is the maximal angle of the
        self.x = 0                      # front axis
        self.y = 0                      # the inicial position of the model is
        self.theta = 0                  # (0,0,0) and the pose is (x,y,theta)
        self.poses = [[],[],[]]         # list od the poses of the model
    def clear(self):
        """Clear the list of poses"""
        self.poses = [[],[],[]]
    def getPose(self):
        """Return que actual pose of the model. The pose is in (x,y,theta) form"""
        return self.poses[0][-1],self.poses[1][-1],self.poses[2][-1]
    def setPose(self,x,y,theta):
        """Define a new pose to the model"""
        self.x = x
        self.y = y
        self.theta = theta
        self.poses[0].append(x)
        self.poses[1].append(y)
        self.poses[2].append(theta)
    def Update(self,x,y,theta):
        """Change the pose of the model adding the parameters to the actual pose"""
        self.x += x
        self.y += y
        self.theta += theta
        self.poses[0].append(self.x)
        self.poses[1].append(self.y)
        self.poses[2].append(self.theta)
    def run(self,v,alpha):
        """Calculate the next pose of the model getting the speed (distance travaled
        in this step time) and the steer angle"""
        if(alpha > self.alpha_max):   #limits the steer angle to the fisical limit
            alpha = self.alpha_max
        if(alpha < -self.alpha_max):
            alpha = -self.alpha_max
        delta_x = v*math.cos(math.radians(self.theta))
        delta_y = v*math.sin(math.radians(self.theta))
        delta_theta = (v/self.L)*math.tan(math.radians(alpha))
        self.Update(delta_x,delta_y,delta_theta)
    def show(self,legend = "Path"):
        """Plot the path of the model"""
        plt.plot(self.poses[0],self.poses[1],label = legend)
        plt.legend()
        plt.draw()
    def sim_RandomPath(self,v,steps):
        """Simulate the model running with const speed (v in meters per step)
         and random steer angle for a number of steps"""
        for i in xrange(steps):
            alpha = random.uniform(-self.alpha_max,self.alpha_max)
            self.run(v,alpha)
    def sim_Path(self,v,alpha):
        """Simulate the path of the model using a list of speeds and angles,
        this lists should have the same length"""
        for i in xrange(len(v)):
            self.run(v[i],alpha[i])
    def __str__(self):
        return str(self.poses)
