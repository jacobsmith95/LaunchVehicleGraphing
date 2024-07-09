import numpy as np


class Rocket():
    """"""

    def __init__(self, mass: float, thrust: float):
        """"""
        self.mass   = mass
        self.weight = mass*(9.80665)
        self.thrust = thrust
        self.ratio  = self.thrust/self.weight
        self.vel    = 0.0
        self.acc    = 0.0
        self.time   = 0.0

    def reduce_mass(self, mass_change: float):
        """"""
        self.mass -= mass_change

    def calculate_vel(self):
        """"""
        self.vel = self.acc*self.time

    def calculate_acc(self, acceleration: float):
        """"""
        self.acc = self.ratio/self.mass

    def change_time(self, new_time: float):
        """"""
        self.time = new_time

    def change_ratio(self):
        """"""
        self.ratio = self.thrust/self.weight

    def return_velocity(self):
        """"""
        return self.vel
