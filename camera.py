import mapping
import matplotlib.pyplot as plt
import math
class Camera(object):
    """Simulate a camera used to read the map"""
    def __init__(self, L = 60):
        self.L = L          #The length of the camera image (pixels)
    def loadMap(self,map):
        self.map = map

    def readLine(self,pose):
        """ Read a line on the map"""
        #Define the position of the first pixel
        startx =  pose[0]+(self.L/2)*math.cos(math.radians(pose[2]+90))
        starty =  pose[1]+(self.L/2)*math.sin(math.radians(pose[2]+90))
        x = []
        y = []
        reads = []

        for i in xrange(self.L):    #run over the line pixel by pixel
            x.append(int(startx+i*math.cos(math.radians(pose[2]-90))))
            y.append(int(starty+i*math.sin(math.radians(pose[2]-90))))
            reads.append(self.map.read(x[-1],y[-1]))
        plt.plot(x,y)
        plt.draw()
        return reads

cam = Camera()
mapa = mapping.Map("Maps/mapa.png")
cam.loadMap(mapa)
print cam.readLine((100,95,90))
cam.map.show()

plt.show()
