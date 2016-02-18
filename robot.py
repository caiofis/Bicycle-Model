import matplotlib.pyplot as plt
import vehicle
import camera
import mapping

class Robot(vehicle.Vehicle):
    """This class take all the previous classes and create a robot model, it can
    see the map over the camera and move based on it"""
    def __init__(self,map_file, cam_length = 60, L = 1 ,alpha_max = 90):
        vehicle.Vehicle.__init__(self,L,alpha_max)
        self.map = mapping.Map(map_file)
        self.cam = camera.Camera(cam_length)
        self.cam.loadMap(self.map)

    def show(self):
        self.map.show()
        vehicle.Vehicle.show(self)
    def pControl(self,Kp = 1,v = 1):
        error = self.cam.findLine(self.getPose())
        alpha = Kp * error
        self.run(v,alpha)
    def sim_LineFollower(self, v = 1 , Kp = 5, Steps = 500):
        for i in xrange(800):
            rob.pControl(Kp,v)

rob = Robot("Maps/mapa.png",L = 0.5,alpha_max=40)
rob.setPose(200,70,0)
rob.sim_LineFollower()
rob.show()
plt.show()
