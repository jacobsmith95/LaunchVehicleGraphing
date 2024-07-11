import numpy as np


def dynamic_pressure(flow_speed: float, altitude: float) -> float:
    """"""
    
    return (0.5)*(_calculate_mass_density(altitude))*(flow_speed**2)


def max_q(q_list: list) -> float:
    """"""


def _calculate_mass_density(altitude: float) -> float:
    """"""
    base_mass_density = _get_mass_density(altitude)
    standard_temperature = _get_standard_temperature(altitude)
    geopotential_height = _get_geopotential_height(altitude)
    if altitude < 11000.01:
        temperature_lapse_rate = _get_standard_temperature_lapse_rate(altitude)
        temperature_term = ((standard_temperature-(altitude-geopotential_height)*temperature_lapse_rate)/(standard_temperature))
        exponent_term = (((9.80665*0.0289644)/(8.3144598*temperature_lapse_rate))-1)
        return base_mass_density*temperature_term**exponent_term
    else:
        exponent_term = ((-9.80665*0.0289644*(altitude-geopotential_height))/(8.3144598*standard_temperature))
        return base_mass_density*(2.7182818284)**exponent_term


def _get_mass_density(altitude: float) -> float:
    """"""
    if 0.00 <= altitude < 11000.0:
        return 1.2250
    if 11000.01 <= altitude < 20000.0:
        return 0.36391
    if 20000.01 <= altitude < 32000.0:
        return 0.08803
    if 32000.01 <= altitude < 47000.0:
        return 0.01322
    if 47000.01 <= altitude < 51000.0:
        return 0.00143
    if 51000.01 <= altitude < 71000.0:
        return 0.00086
    if 71000.01 <= altitude:
        return 0.000064
    

def _get_standard_temperature(altitude: float) -> float:
    """"""
    if 0.00 <= altitude < 11000.0:
        return 288.15
    if 11000.01 <= altitude < 20000.0:
        return 216.65
    if 20000.01 <= altitude < 32000.0:
        return 216.65
    if 32000.01 <= altitude < 47000.0:
        return 228.65
    if 47000.01 <= altitude < 51000.0:
        return 270.65
    if 51000.01 <= altitude < 71000.0:
        return 270.65
    if 71000.01 <= altitude:
        return 214.65
    

def _get_standard_temperature_lapse_rate(altitude: float) -> float:
    """"""
    if 0.00 <= altitude < 11000.0:
        return 0.0065
    if 11000.01 <= altitude < 20000.0:
        return 0.0
    if 20000.01 <= altitude < 32000.0:
        return -0.001
    if 32000.01 <= altitude < 47000.0:
        return -0.0028
    if 47000.01 <= altitude < 51000.0:
        return 0.0
    if 51000.01 <= altitude < 71000.0:
        return 0.0028
    if 71000.01 <= altitude:
        return 0.002
    

def _get_geopotential_height(altitude: float) -> float:
    """"""
    if 0.00 <= altitude < 11000.0:
        return 0
    if 11000.01 <= altitude < 20000.0:
        return 11000.0
    if 20000.01 <= altitude < 32000.0:
        return 20000.0
    if 32000.01 <= altitude < 47000.0:
        return 32000.0
    if 47000.01 <= altitude < 51000.0:
        return 47000.0
    if 51000.01 <= altitude < 71000.0:
        return 51000.0
    if 71000.01 <= altitude:
        return 71000.0
    
