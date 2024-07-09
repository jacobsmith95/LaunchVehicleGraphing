import numpy as np


class Rocket():
    """"""

    def __init__(self, mass: float):
        """"""
        self.mass = mass
        self.vel  = 0.0
        self.acc  = 0.0

    def reduce_mass(self, mass_change: float):
        """"""
        self.mass -= mass_change

    def change_vel(self, velocity: float):
        """"""
        self.vel = velocity

    def change_acc(self, acceleration: float):
        """"""
        self.acc = acceleration
        