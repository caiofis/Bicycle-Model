
import numpy as np
import random
import matplotlib.pyplot as plt
import kalman
""" This example shows a basic implematation of the Kalman Filter Class,
    its filter a one dimension measure to a one dimension state """
voltimeter = kalman.Kalman()    # create a kalman object
x = range(100)                  # number of measurements
z=[]                            # list of measurements
voltage = 3                     # real valor of the voltage
for i in x:
    z.append( voltage + np.random.normal(0,0.5))  #add noise to the measure
    voltimeter.Step(0,z[i])                       #estimate the voltage value

#plot the results
plt.axis([0, 100, 0, 6])
print voltimeter.states
plt.plot(x,z,label = "Measurements")
plt.plot(x,voltimeter.states,label = "Kalman filtered")
plt.show()
