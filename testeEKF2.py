import matplotlib.pyplot as plt
import robot
import numpy as np
import EKF
import upper_cam

"""Inicialize the Robot in the map and run it autonomous"""
rob = robot.Robot("Maps/mapao.png",alpha_max=30) #inicialize the robot in the map
rob.setOdometry(True)                 #configure its odometer
rob.setOdometryVariance([0.01,0.3])
rob.setPose(400,400,0)              #set a initial pose
rob.sim_LineFollower(Steps = 180 ,Kp=1,Kd=0.3,v=0.05,debug=False)
speed , angle =  rob.readOdometry()       #reads the sensors

"""Set the upper cam to read the robot pose and corrup it with noise"""
cam = upper_cam.UpperCam([10,10,0.5],rob)
cam.readPath()
camPoses = cam.readPoses()

"""Create two EKFs to estimate the robot pose.
    The frist one will do it without any update info, the second will use the 
    upper cam."""
x = np.array([400,400,0])
P = np.zeros((3,3))
V = np.diag([(0.01*370)**2,(0.5*3.14/180)**2])
R = np.diag([35**2,35**2,2**2])
EKF1 = EKF.EKF(x,P,V,R,L=0.2*370)  #Create a Kalman filter for the odometry
EKF2 = EKF.EKF(x,P,V,R,L=0.2*370)  #Create a Kalman filter for the odometry

poses1 = [[],[]]
poses2 = [[],[]]
P1_ = []
for i in range(len(speed)):
    poses1[0].append(x[0])
    poses1[1].append(x[1])
    EKF1.Prediction([speed[i]*370,angle[i]*0.01745])
    x = EKF1.x
    #P1_.append((EKF.P[0][0])**0.5)
x = np.array([400,400,0])
for i in range(len(speed)):
    EKF2.Prediction([speed[i]*370,angle[i]*0.01745])
    EKF2.Update([camPoses[0][i],camPoses[1][i],camPoses[2][i]*0.01745])
    x = EKF2.x
    poses2[0].append(x[0])
    poses2[1].append(x[1])
    
    
rob.show()  #plot the results
plt.plot(poses1[0],poses1[1],'g',label = "Odometry")
plt.plot(poses2[0],poses2[1],'r',label = "Kalman")
plt.plot(camPoses[0],camPoses[1],marker = '+',linestyle = 'None',color = 'magenta',label = "UpperCam")
plt.legend()
plt.show()
#plt.plot(range(len(speed)),P1_)
