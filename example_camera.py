import camera
import mapping
import matplotlib.pyplot as plt

cam = camera.Camera(0.2,30,300)         #Create a camera 300 pix wide
mapa = mapping.Map("Maps/mapa2.png")    #Create a map
cam.loadMap(mapa)                       #Load the map into the camera class
pose = (195,200,90)                     #define the pose of the camera
print cam.readLine(pose,visualize = True)#print the raw camara read
print cam.findPath(pose)                #print the diference from the pose
                                        # to the center of the path

#Plot the results
cam.map.show()
plt.show()
