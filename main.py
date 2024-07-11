import numpy as np
import matplotlib.pyplot as plt
from DynamicPressure import *
from ModelRocket import Rocket


#r1 = Rocket(30000, 2256, 1.0)

def get_pressure(time):
    """"""
    r1.change_time(time)
    r1.calculate_mass()
    r1.calculate_acc()
    r1.calculate_vel()
    velocity = r1.get_velocity()
    r1.calculcate_alt()
    altitude = r1.get_altitude()
    pressure = dynamic_pressure(velocity, altitude)
    dynamic_pressure_list.append(pressure)
    #r1.change_time(time)
    #return pressure

r1 = Rocket(5000000, 74400, 1.0)
x = np.arange(0.0, 4000.0, .1)
dynamic_pressure_list = []
for num in x:
    get_pressure(num)
fig, ax = plt.subplots()
ax.plot(x, dynamic_pressure_list)
plt.show()
