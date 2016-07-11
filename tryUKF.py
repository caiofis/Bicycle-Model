# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:33:07 2016

@author: caio
"""
import vehicle
import matplotlib.pyplot as plt
import upper_cam
import numpy as np
import math
from filterpy.kalman import MerweScaledSigmaPoints
from filterpy.kalman import UnscentedKalmanFilter as UKF

def state_mean(sigmas, Wm):
    x = np.zeros(3)
    sum_sin, sum_cos = 0., 0.

    for i in range(len(sigmas)):
        s = sigmas[i]
        x[0] += s[0] * Wm[i]
        x[1] += s[1] * Wm[i]
        sum_sin += np.sin(s[2])*Wm[i]
        sum_cos += np.cos(s[2])*Wm[i]
    x[2] = np.arctan2(sum_sin, sum_cos)
    return x
def normalize_angle(x):
    x = x % (2 * np.pi)    # force in range [0, 2 pi)
    if x > np.pi:          # move to [-pi, pi)
        x -= 2 * np.pi
    return x
def residual(a, b):
    y = a - b
    y[2] = normalize_angle(y[2])
    return y
def f(x,dt,u):
        """Estimate the non-linear state of the system"""
        #print ((u[0]/self.L)*math.tan(u[1]))
        return np.array([x[0]+u[0]*math.cos(x[2]),
                         x[1]+u[0]*math.sin(x[2]),
                         x[2]+((u[0]/1)*math.tan(u[1]))])
def h(z):
    return z               
points = MerweScaledSigmaPoints(3,.001,2.,0.)
filter = UKF(3,3,0,h, f, points, sqrt_fn=None, x_mean_fn=state_mean, z_mean_fn=state_mean, residual_x=residual, residual_z=residual)
filter.P = np.diag([0.04,0.04,1])
filter.Q = np.diag([(0.2)**2,(0.2)**2,(1*3.14/180)**2])
filter.R = np.diag([100,100,0.25])
robot = vehicle.Vehicle(1,50)           #create a robot
robot.setOdometry(True)                 #configure its odometer
robot.setOdometryVariance([0.2,1])
speed,angle = [],[]
for a in xrange(4):                     #create a retangular path
    for i in xrange(400):
        angle.append(0)
    for i in xrange(9):
        angle.append(10)

for i in xrange(len(angle)):        #set the speed to a constant along the path
    speed.append(1)

robot.sim_Path(speed,angle)             #run in a rectangular path
speed , angle =  robot.readOdometry()       #reads the sensors
cam = upper_cam.UpperCam([10,10,0.5],robot)
cam.readPath()
camPoses = cam.readPoses()
Uposes = [[],[]]
for i in range(len(speed)):
    x = filter.x
    #print x
    Uposes[0].append(x[0])
    Uposes[1].append(x[1])
    filter.predict(fx_args=[speed[i],angle[i]*0.01745])
    filter.update(z = [camPoses[0][i],camPoses[1][i],camPoses[2][i]*0.01745])
#robot.show("Real")
plt.plot(Uposes[0],Uposes[1],'y',label = "UKF")
plt.legend()
plt.show()