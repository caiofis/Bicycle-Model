import matplotlib.pyplot as plt
import robot

"""This example show a tipical use of the "Robot" Class, it loads a image file
thats represent the road's map and run over it using a PID control.
The plot is scale using the default pixels per meter value (370)"""

rob = robot.Robot("Maps/mapao.png",alpha_max=30) #inicialize the robot in the map
rob.setPose(400,400,0)              #set a initial pose
rob.sim_LineFollower(Steps = 1000 ,Kp=1,Kd=0.3,v=0.04,debug=True)
""" This method apply the PID control to the model, its print the error read by
the camera and the value applied to the steer angle, the angle is find as the
value * alpha_max"""
rob.show()  #plot the results
plt.show()
