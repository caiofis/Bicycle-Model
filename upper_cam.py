import random
import robot

class UpperCam(object):
    """Implement a  UpperCamera to see the pose of the robot"""
    def __init__(self, robot,covariance):
        self.robot = robot
        self.covariance = covariance
    def getPose(self):
    #""" Return de real pose corrupted by a gaussian noise with zero mean and
    #variance defined by the covariance matrix"""
        measurement = []
        real = self.robot.getPose()
        for i in range(len(real)):
            measurement.append(real[i] + random.gauss(0,self.covariance[i]))
        return measurement
