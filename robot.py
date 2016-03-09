import matplotlib.pyplot as plt
import math
import bicycle
import vehicle
import camera
import mapping

class Robot(vehicle.Vehicle):
    """This class take all the previous classes and create a robot model, it can
    see the map over the camera and move based on it"""
    def __init__(self,map_file, cam_length = 128, L = 0.2 ,alpha_max = 20,
                                                    pxlpermeter = 370):
        vehicle.Vehicle.__init__(self,L,alpha_max)      #create a vehicle
        self.pxlpermeter = pxlpermeter                  #scale the plot
        self.map = mapping.Map(map_file)                #create a map
        self.cam = camera.Camera(cam_length)            #Load the map into the
        self.cam.loadMap(self.map)                      #robots camera
        self.error = 0                                  #actual error (error[k])
        self.last_error = 0                             #last error (error[k-1])
        self.int_error = 0                              #integral of the error

    def run(self,v,value):
        '''Sobrepose the run method applying the pixels per meter paramater and
        to scale the angle as a value from -1 to 1'''
        ###Value must be between -1 and 1
        self.Odometry(v,value)        #Reads the odometry sensors
        alpha = value*self.alpha_max  #scale the value to the steer angle
        v = v*self.pxlpermeter
        bicycle.Bicycle.run(self,v,alpha)
    def show(self,legend = "Path"):
        """Show the image of the map and the poses of the robot"""
        self.map.show()
        bicycle.Bicycle.show(self,legend)
    def pidControl(self,Kp = 2,Ki = 0, Kd = 0,v = 1,debug=False):
        """Aplly the PID control to the model"""
        error = self.cam.findLine(self.getPose(),visualize=False)
        self.int_error += error
        delta_error = error - self.last_error
        last_error = error
        alpha = Kp * error + Ki * self.int_error + Kd * delta_error
        self.run(v,alpha)
        if debug:
            print error,alpha
    def sim_LineFollower(self,Kp = 2, Ki = 0, Kd = 0, v =5, Steps = 500,debug=False):
        for i in xrange(Steps):
            self.pidControl(Kp,Ki,Kd,v,debug)
