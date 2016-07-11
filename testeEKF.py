import vehicle
import matplotlib.pyplot as plt
import EKF
import numpy as np
import upper_cam
""" Simulate a robot in a rectangular path then draw the path read direct from the
    odometry with no filter"""

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

x = np.zeros(3)
P = np.zeros((3,3))
V = np.diag([(0.2)**2,(1*3.14/180)**2])
R = np.diag([10**2,10**2,2**2])
EKF1 = EKF.EKF(x,P,V,R,L=1)  #Create a Kalman filter for the odometry
EKF2 = EKF.EKF(x,P,V,R,L=1)  #Create a Kalman filter for the odometry
cam = upper_cam.UpperCam([10,10,0.5],robot)
cam.readPath()
camPoses = cam.readPoses()

Pposes = [[],[]]
Uposes = [[],[]]
P_ = []
P2_ = []
noiseposes = [[],[],[]]
for i in range(len(speed)):
    Pposes[0].append(x[0])
    Pposes[1].append(x[1])
    EKF1.Prediction([speed[i],angle[i]*0.01745])
    #EKF.Update(cam.noisePose([robot.poses[0][i],robot.poses[1][i],robot.poses[2][i]*0.01745]))
    x = EKF1.x
    P_.append((np.linalg.det(EKF1.P))**0.5)
for i in range(len(speed)):
    EKF2.Prediction([speed[i],angle[i]*0.01745])
    EKF2.Update([camPoses[0][i],camPoses[1][i],camPoses[2][i]*0.01745])
    x = EKF2.x
    Uposes[0].append(x[0])
    Uposes[1].append(x[1])
    P2_.append((np.linalg.det(EKF2.P))**0.5)
#show the paths
robot.show("Real")
plt.plot(camPoses[0],camPoses[1],marker = '+',linestyle = 'None',color = 'magenta',label = "UpperCam")
plt.plot(Pposes[0],Pposes[1],label = "Odometry")
plt.plot(Uposes[0],Uposes[1],'k',label = "Kalman")
plt.show()
#Show Errors
#plt.plot(range(len(speed)),P_)
#plt.plot(range(len(speed)),P2_)
#plt.show()