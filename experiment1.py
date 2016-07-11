# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 12:55:29 2016

@author: caio
"""

import experiment_functions as func
EKFdist = 0
UKFdist = 0
for i in range(1):
    real, camPoses = func.generatePath()
    EKFposes = func.estimateEKF(camPoses)
    UKFposes = func.estimateUKF(camPoses)
    EKFdist += func.euclideanDist(real,EKFposes)/1
    UKFdist += func.euclideanDist(real,UKFposes)/1

plt.plot(range(len(EKFdist)),EKFdist,'g', label = "EKF")
plt.plot(range(len(UKFdist)),UKFdist,'r', label = "UKF")
plt.ylim((2.5,3.5))
plt.legend()
#plt.plot(real[0],real[1],'b', label = "Real")
#plt.plot(EKFposes[0],EKFposes[1],'g',label = "EKF")
#plt.plot(UKFposes[0],UKFposes[1],'r',label = "UKF")