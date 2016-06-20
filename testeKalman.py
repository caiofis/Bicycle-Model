import matplotlib.pyplot as plt
import vehicle
import EKF
import numpy as np
import math

def dist(real,noizy,steps):
#"Define the metric of the error between the real and the noizy estimated"
    error = []
    for i in xrange(len(real[0])):
        #print i
        dist = 0
        distx = ((float(real[0][i])-float(noizy[0][i])))**2#/float(real[0][i]))**2
        disty = ((float(real[1][i])-float(noizy[1][i])))**2#/float(real[1][i]))**2
        disttheta = (0.01745*(float(real[2][i]))-float(noizy[2][i]))**2
        dist = ((distx+disty)**(0.5))
        error.append(dist)
    return error

car = vehicle.Vehicle(L = 0.2,alpha_max = 20)
car.setOdometry(True)
car.setOdometry([0.05,0.5])#*3.14/180
#car.setOdometry([0,0])
P = np.diag([0.00005,0.00005,0.008])
V = np.diag([(0.05)**2,(0.5*3.14/180)**2])
speed,angle = [],[]
for a in xrange(4):                     #create a retangular path
    for i in xrange(400):
        angle.append(0)
    for i in xrange(7):
        angle.append(5)

for i in xrange(len(angle)):        #set the speed to a constant along the path
    speed.append(0.5)
car.sim_Path(speed,angle)
kalman = EKF.EKF()
x = [0,0,0]
u = car.readOdometry()
uncertainty = []
poses=[[],[],[]]
#print len(u[0])
for a in xrange(len(u[0])):
    poses[0].append(x[0])
    poses[1].append(x[1])
    poses[2].append(x[2])
    u_ = [float(u[0][a])+np.random.normal(0,0.05),(float(u[1][a])+np.random.normal(0,0.5))*0.01745]
    print u_
    x,P = kalman.Prediction(x,u_,P,V)
    uncertainty.append((P[0][0]+P[1][1])**0.5)#
#print poses
#print car.poses
car.show()
plt.plot(poses[0],poses[1])
plt.show()
error = dist(car.poses,poses,len(poses[0]))
plt.plot(range(len(uncertainty)), uncertainty)
plt.plot(range(len(error)),error)
plt.show()
