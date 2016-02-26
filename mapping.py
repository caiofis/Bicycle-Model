import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class Map(object):
    """This class create a representation of the robot environmet receving an
    image of its map, the image is converted to a black and white image and then
    represented as a numpy array"""
    def __init__(self,file):
        """ Create the map based in the image file"""
        self.pixels = np.asarray(Image.open(file).convert("L").transpose(Image.FLIP_TOP_BOTTOM))
    def show(self):
        """Plot the image as a b&w plot"""
        plt.imshow(self.pixels)#, interpolation='nearest')
        plt.axis([0,self.pixels[0].size,0,self.pixels.size/self.pixels[0].size])
        plt.gray()
        plt.draw()
    def read(self,x,y):
        return self.pixels[y][x]
    def getMap(self):
        return self.pixels



# mapa = Map("Maps/mapa.bmp")
#
# mapa.show()
# plt.show()
