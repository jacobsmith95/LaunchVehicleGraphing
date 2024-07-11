import numpy as np


class Rocket():
    """"""

    def __init__(self, mass: float, thrust: float, mdot: float):
        """"""
        self.mass   = mass
        self.weight = (mass*(9.80665))/1000
        self.thrust = thrust
        self.mdot   = mdot
        self.vel    = 0.0
        self.acc    = 0.0
        self.time   = 0.0
        self.alt    = 0.0

    def calculate_mass(self):
        """"""
        self.mass = self.mass - (self.mdot*self.time)
        if self.mass <= 0.0:
            self.mass = 0.1

    def calculate_vel(self):
        """"""
        self.vel = self.acc*self.time

    def calculate_acc(self):
        """"""
        self.acc = (self.thrust-self.weight)/self.mass

    def calculcate_alt(self):
        """"""
        self.alt = (0.5)*(self.acc)*(self.time**2)

    def change_time(self, new_time: float):
        """"""
        self.time = new_time

    def get_velocity(self):
        """"""
        return self.vel
    
    def get_altitude(self):
        """"""
        return self.alt
