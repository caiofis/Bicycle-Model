import random

class UpperCam(object):
    """Implement a  UpperCamera to see the pose of the robot"""
    def __init__(self, covariance,robot = None):
        self.robot = robot
        self.covariance = covariance
        self.poses = [[],[],[]]
    def getPose(self):
    #""" Return de real pose corrupted by a gaussian noise with zero mean and
    #variance defined by the covariance matrix"""
        measurement = []
        real = self.robot.getPose()
        for i in range(len(real)):
            self.poses[i].append(real[i] + random.gauss(0,self.covariance[i]))
            measurement.append(self.poses[i][-1])
        return measurement
    def noiseSinglePose(self,pose):
        measurement = []
        real = pose
        for i in range(len(real)):
            self.poses[i].append(real[i] + random.gauss(0,self.covariance[i]))
            measurement.append(self.poses[i][-1])
        return measurement
    def readPath(self):
        """Read the enter path of the robot and noise the poses.
            The result is save in the the class"""
        for i in xrange(len(self.robot.poses[0])):
            self.noiseSinglePose([self.robot.poses[0][i],self.robot.poses[1][i],
                             self.robot.poses[2][i]])
    def readPoses(self):
        return self.poses

#cam = UpperCam([10,10,10])
#cam.noisePose([0,0,0])