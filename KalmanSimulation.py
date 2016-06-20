import matplotlib.pyplot as plt
import csv
import vehicle
import EKF
import numpy as np
import math
def openCSV():
    "Load a csv file of simulations"
    file = open('simulations.csv', 'rb')
    reader = csv.reader(file,delimiter = ',')
    "Load the true values"
    for i in xrange(3):
        reader.next()       #Discart the header
        real.append(reader.next())
    print "Real Loaded"
    for i in xrange(1):
        reader.next()       #Discart the header
        u[0] = reader.next()
        reader.next()       #Discart the header
        u[1] = reader.next()

def dist(real,noizy,steps):
#"Define the metric of the error between the real and the noizy estimated"
    error = []
    for i in xrange(len(real[0])-1):
        #print i
        dist = 0
        distx = ((float(real[0][i])-float(noizy[0][i])))**2#/float(real[0][i]))**2
        disty = ((float(real[1][i])-float(noizy[1][i])))**2#/float(real[1][i]))**2
        dist = ((distx+disty)**(0.5))
        error.append(dist)
    return error

u= [0,0]
real = []
openCSV()
kalman = EKF.EKF()
x_ = np.array([float(real[0][0]),float(real[1][0]),float(real[2][0])])
#x_ = np.array([0,0,0])
P_ = np.array([[0,0,0],[0,0,0],[0,0,0]])
V = np.array([[0.000025,0],[0,(0.5*3.14/180)**2]])
uncertainty = []
poses = [[],[]]
#x_[2] = (x_[2])
for a in xrange(len(u[0])):
     poses[0].append(x_[0])
     poses[1].append(x_[1])
     u_ = [float(u[0][a]),float(u[1][a])]#*3.14/180]
     #u_[1] = math.radians(u_[1])
     #u_ = [0.05,0.1]
     print x_
     print u_
     x_,P_ = kalman.Prediction(x_,u_,P_,V)
     print x_
     uncertainty.append((P_[0][0])**0.5)

#
plt.plot(poses[0],poses[1])
plt.show()
#error = dist(real,poses,1)
#plt.plot(range(len(error)),error)
plt.plot(range(len(uncertainty)), uncertainty)
plt.show()
