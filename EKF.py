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
        return np.array([[math.cos(math.radians(x[2])), -u[0]*math.sin(math.radians(x[2]))],
                         [math.sin(math.radians(x[2])),  u[0]*math.cos(math.radians(x[2]))],
                         [      0       ,               1                   ]])
    def f(self,x,u):
        """Estimate the non-linear state of the system"""
        return np.array([x[0]+u[0]*math.cos(math.radians(x[2])),
                         x[1]+u[0]*math.sin(math.radians(x[2])),
                         x[2]+(u[0]/self.L)*math.tan(math.radians(u[1]))])
    def Prediction(self,x,u,P,V):
        x_ = self.f(x,u)
        P_ = self.Fx(x_,u).dot(P).dot(np.transpose(self.Fx(x_,u))) + \
             self.Fu(x_,u).dot(V).dot(np.transpose(self.Fu(x_,u)))
        return x_,P_
kalman = EKF()
x = np.array([10,0,0])
u = np.array([1,-10,1])
P = np.array([[1,1,1],[1,1,1],[1,1,1]])
V = np.array([[1,1],[1,1]])
x_,P_ = kalman.Prediction(x,u,P,V)
print P_
x_,P_ = kalman.Prediction(x_,u,P_,V)
print P_
