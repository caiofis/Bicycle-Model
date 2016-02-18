import matplotlib.pyplot as plt
import vehicle
import camera
import mapping

class Robot(vehicle.Vehicle):
    """This class take all the previous classes and create a robot model, it can
    see the map over the camera and move based on it"""
    def __init__(self,map_file, cam_length = 60, L = 1 ,alpha_max = 90):
        vehicle.Vehicle.__init__(self,L,alpha_max)      #create a vehicle
        self.map = mapping.Map(map_file)                #create a map
        self.cam = camera.Camera(cam_length)            #Load the map into the
        self.cam.loadMap(self.map)                      #robots camera
        self.error = 0                                  #actual error (error[k])
        self.last_error = 0                             #last error (error[k-1])
        self.int_error = 0                              #integral of the error

    def show(self):
        self.map.show()
        vehicle.Vehicle.show(self)
    def pidControl(self,Kp = 2,Ki = 0, Kd = 0,v = 1):
        """Aplly the PID control to the model"""
        error = self.cam.findLine(self.getPose())
        self.int_error += error
        delta_error = error - self.last_error
        last_error = error
        alpha = Kp * error + Ki * self.int_error + Kd * delta_error
        self.run(v,alpha)

    def sim_LineFollower(self,Kp = 2, Ki = 0, Kd = 0, v =5, Steps = 500):
        for i in xrange(Steps):
            self.pidControl()

rob = Robot("Maps/mapao.png",L = 1,alpha_max=60)
rob.setPose(400,400,0)
rob.sim_LineFollower(Steps = 3000)
rob.show()
plt.show()
