def convert_flow_rate(value,from_unit):
    conversion_factors = {
        "m3/s": 1.0,
        "m3/hr": (1/3600.0),
        "L/s": 0.001,
        "L/min": (1/60000.0)
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported flow rate unit: {from_unit}")
    return value * conversion_factors[from_unit]
def convert_length(value,from_unit):
    conversion_factors = {
        "m": 1.0,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported length unit: {from_unit}")
    return value * conversion_factors[from_unit]
def convert_pressure(value,from_unit):
    conversion_factors = {
        "Pa": 1.0,
        "kPa": 1000.0,
        "MPa": 1e6,
        "bar": 1e5,
        "psi": 6894.76
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported pressure unit: {from_unit}")
    return value * conversion_factors[from_unit]
def convert_density(value,from_unit):
    conversion_factors = {
        "kg/m3": 1.0,
        "g/cm3": 1000.0,
        "lb/ft3": 16.0185
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported density unit: {from_unit}")
    return value * conversion_factors[from_unit]
def convert_viscosity(value,from_unit):
    conversion_factors = {
        "Pa·s": 1.0,
        "cP": 0.001
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported viscosity unit: {from_unit}")
    return value * conversion_factors[from_unit]
def convert_velocity(value,from_unit):
    conversion_factors = {
        "m/s": 1.0,
        "cm/s": 0.01,
        "mm/s": 0.001,
        "in/s": 0.0254,
        "ft/s": 0.3048
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported velocity unit: {from_unit}")
    return value * conversion_factors[from_unit]