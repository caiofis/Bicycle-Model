import numpy as np
import math

class EKF(object):
    """Implements an EKF to the localization of the famous bicycle model.
    Ist control inputs must be in meters and radians, as well for its state."""
    def __init__(self,x,P,V,R=0,L=0.2):
        self.L=L        #Set the distance between the wheels
        self.x = x      #Set the initial state
        self.P = P      #Set the initial Covariance
        self.V = V      #Set the process noise covariance
        self.R = R      #Set the measurement noise covariance
    def Fx(self,x,u):
        """Linearize the system with the Jacobian of the x"""
        return np.array([[1,0,-u[0]*math.sin(x[2])],
                         [0,1, u[0]*math.cos(x[2])],
                         [0,0, 1                  ]])
    def Fu(self,x,u):
        """Linearize the system with the Jacobian of the u"""
        return np.array([[math.cos(x[2]), 0],#-u[0]*math.sin((x[2]+u[1]))],
                         [math.sin(x[2]), 0],   #  u[0]*math.cos((x[2]+u[1]))],
                         [math.tan(u[1])/self.L, (u[0]/self.L)*(1/math.cos(u[1]))**2]])
    def f(self,x,u):
        """Estimate the non-linear state of the system"""
        #print ((u[0]/self.L)*math.tan(u[1]))
        return np.array([x[0]+u[0]*math.cos(x[2]),
                         x[1]+u[0]*math.sin(x[2]),
                         x[2]+((u[0]/self.L)*math.tan(u[1]))])
    def H(self):
        """Linearize the measurement function"""
        return np.eye(3)
    def h(self,x):
        return x

    def Prediction(self,u):
        #u[1] = ((u[0]/self.L)*math.tan((u[1])))
        x_ = self.x
        P_ = self.P
        self.x = self.f(x_,u)
        self.P = self.Fx(x_,u).dot(P_).dot((self.Fx(x_,u)).T) + \
             self.Fu(x_,u).dot(self.V).dot((self.Fu(x_,u)).T)
    def Update(self, z):
        """Update the Kalman Prediction using the meazurement z"""
        y = z - self.h(self.x)
        K = self.P.dot(np.linalg.inv(self.P+self.R))
        self.x = self.x + K.dot(y)
        self.P = (np.eye(3)-K).dot(self.P)
#V = np.diag([(0.05)**2,(0.5*3.14/180)**2])
#kalman = EKF(np.zeros(3),np.zeros((3,3)),V,L=1)
#kalman.Prediction([1,0.2])