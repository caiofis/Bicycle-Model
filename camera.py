import mapping
import matplotlib.pyplot as plt
import math

class Camera(object):
    """Simulate a line scan camera used to read the map

    **L** is length of the camera image in pixels"""
    def __init__(self, H, cam_angle, L = 60):
        self.L = L          #The length of the camera image (pixels)
        self.H = H
        self.cam_angle= cam_angle
        self.error = 0
    def loadMap(self,map):
        """Load a Map object into the camera"""
        self.map = map

    def readLine(self,pose,visualize = False):
        """Reads a line of the map based on the pose of the robot"""
        #Define the distance between the robot and the camera readLine
        d_cam = self.H * math.tan(math.radians(self.cam_angle))
        #Define the position of the first pixel
        startx =  (pose[0] + d_cam*math.cos((pose[2]))) + \
         (self.L/2)*math.cos((pose[2]+1.5708))
        starty =  (pose[1] + d_cam*math.sin((pose[2]))) + \
        (self.L/2)*math.sin((pose[2]+1.5708))
        x = []      #list of x positions of the pixels
        y = []      #list of y positions of the pixels
        reads = []  #value of the pixels

        for i in xrange(self.L):    #run over the line pixel by pixel
            x.append(int(startx+i*math.cos((pose[2]-1.5708))))
            y.append(int(starty+i*math.sin((pose[2]-1.5708))))
            reads.append(self.map.read(x[-1],y[-1]))
        if visualize:
            plt.plot(x,y)
            plt.draw()
        return reads
    def findLine(self,pose,visualize = False):
        """ Finds the center of a black line in the image read by the models pose
        and return the diference from it to the center of the camera in a range
        from -1 to 1

        - If no line is found its return the last error

        - Find de centroid of the black points in the image, this is the center of the line by definition, and compare with the center of the camera length"""
        address = 0         #Store the address of the black points
        num = 0             #Store the number of black points find
        read = self.readLine(pose,visualize)  #read the line from the pose of the model
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
        return self.error/float(self.L/2)
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
