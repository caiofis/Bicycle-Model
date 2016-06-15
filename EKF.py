import numpy as np
import math

class EKF(object):
    """docstring for EKF"""
    def __init__(self,L=0.2):
        self.L=L
    def Fx(self,x,u):
        """Linearize the system with the Jacobian of the x"""
        return np.array([[1,0,-u[0]*math.sin(math.radians(x[2]))],
                         [0,1, u[0]*math.cos(math.radians(x[2]))],
                         [0,0, 1                  ]])
    def Fu(self,x,u):
        """Linearize the system with the Jacobian of the u"""
        return np.array([[math.cos(math.radians(x[2])), 0],#-u[0]*math.sin(math.radians(x[2]+u[1]))],
                         [math.sin(math.radians(x[2])), 0],   #  u[0]*math.cos(math.radians(x[2]+u[1]))],
                         [math.tan(math.radians(u[1]))/self.L, (u[0]/self.L)*(1/(math.cos(math.radians(u[1]))))**2]])
    def f(self,x,u):
        """Estimate the non-linear state of the system"""
        return np.array([x[0]+u[0]*math.cos(math.radians(x[2])),
                         x[1]+u[0]*math.sin(math.radians(x[2])),
                         x[2]+u[0]/self.L*math.tan(math.radians(u[1]))])

    def Prediction(self,x,u,P,V):
        #u[1] = ((u[0]/self.L)*math.tan(math.radians(u[1])))
        x_ = self.f(x,u)
        P_ = self.Fx(x_,u).dot(P).dot((self.Fx(x_,u)).T) + \
             self.Fu(x_,u).dot(V).dot((self.Fu(x_,u)).T)
        return x_,P_

# kalman = EKF()
# P=np.array([[1,0,0],[0,1,0],[0,0,1]])
# V=np.array([[1,0],[0,1]])
# print (kalman.Fx([0,0,0],[0.5,0]))
# print kalman.Fu([0,0,0],[0.5,30])
# x , P = kalman.Prediction([0,0,0],[0.5,30],P,V)
# print P
