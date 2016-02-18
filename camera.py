import mapping
import matplotlib.pyplot as plt
import math

class Camera(object):
    """Simulate a camera used to read the map"""
    def __init__(self, L = 60):
        self.L = L          #The length of the camera image (pixels)
        self.error = 0
    def loadMap(self,map):
        self.map = map

    def readLine(self,pose,visualize = False):
        """ Read a line on the map"""
        #Define the position of the first pixel
        startx =  pose[0]+(self.L/2)*math.cos(math.radians(pose[2]+90))
        starty =  pose[1]+(self.L/2)*math.sin(math.radians(pose[2]+90))
        x = []      #list of x positions of the pixels
        y = []      #list of y positions of the pixels
        reads = []  #value of the pixels

        for i in xrange(self.L):    #run over the line pixel by pixel
            x.append(int(startx+i*math.cos(math.radians(pose[2]-90))))
            y.append(int(starty+i*math.sin(math.radians(pose[2]-90))))
            reads.append(self.map.read(x[-1],y[-1]))
        if visualize:
            plt.plot(x,y)
            plt.draw()
        return reads
    def findLine(self,pose):
        """Find de centroid of the black points in the image, this is the center
            of the line by definition, and compare with the center of the camera
            length"""
        address = 0         #Store the address of the black points
        num = 0             #Store the number of black points find
        read = self.readLine(pose)  #read the line from the pose of the model
        for i in xrange(self.L-1):  #run over the read array
            if (read[i] < 150):     #if the pixel value < 150 it is black
                address += i
                num += 1

        #determine the dif between the center fo the camera and the centroid
        #of the black pixels
        # If the line is by the rigth of the center the error is negative
        if(num<1):
            self.error = self.error
        else:
            centroid = address/num      #find the centroid of the black pixels
            self.error=(self.L/2)-centroid
        return self.error
    def findPath(self,pose):
        address = 0         #Store the address of the black points
        read = self.readLine(pose)  #read the line from the pose of the model
        for i in xrange(self.L/2,0,-1):
            if(read[i]<150):
                address = i
                break
        for i in xrange(self.L/2,self.L-1,1):
            a = 0
            if(read[i]<150):
                address += i
                break
        centroid = address/2
        self.error = (self.L/2)-centroid
        return self.error
