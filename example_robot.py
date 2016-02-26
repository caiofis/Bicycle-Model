import matplotlib.pyplot as plt
import robot
"""This example show a tipical use of the "Robot" Class, it loads a image file
thats represent the road's map and run over it using a PID control.
The plot is scale using the default pixels per meter value (370)"""

rob = robot.Robot("Maps/mapao.png")
rob.setPose(400,400,0)
rob.sim_LineFollower(Steps = 1600,Kp=0.1,Kd=0.15,v=0.005)
rob.show()
plt.show()
