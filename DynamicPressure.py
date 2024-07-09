import numpy as np


def dynamic_pressure(flow_speed: float, altitude: float) -> float:
    """"""
    dnp = (0.5)*(_get_mass_density(altitude))*(flow_speed^2)


def max_q(q_list: list) -> float:
    """"""


def _get_mass_density(altitude: float) -> float:
    """"""
    if 0.0 <= altitude <= 11000.0:
        return 1.2250
    if 11000.01 <= altitude <= 20000.0:
        return 0.36391
    if 20000.01 <= altitude <= 32000.0:
        return 0.08803
    if 32000.01 <= altitude <= 47000.0:
        return 0.01322
    if 47000.01 <= altitude <= 51000.0:
        return 0.00143
    if 51000.01 <= altitude <= 71000.0:
        return 0.00086
    if 71000.01 <= altitude:
        return 0.000064
