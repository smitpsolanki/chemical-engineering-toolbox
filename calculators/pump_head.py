from config import LINE_WIDTH
from utils.input_helpers import get_float
from utils.units import convert_density, convert_pressure
from utils.validation import get_positive_float
from utils.input_helpers import select_option
def pump_calculator():
    print("\nPump Head Calculator")
    pressure_drop = get_positive_float("\nEnter the pressure drop across the pump: ")
    pressure_unit = select_option("Select the unit for pressure drop:", ["Pa", "kPa", "MPa", "bar", "psi"])
    pressure_drop = convert_pressure(pressure_drop, pressure_unit)
    density = get_positive_float("\nEnter the density of the fluid: ")
    density_unit = select_option("Select the unit for density:", ["kg/m3", "g/cm3", "lb/ft3"])
    density = convert_density(density, density_unit)
    pump_head = pressure_drop / (density * 9.81)
    print("\nUsing equation:")
    print("\nHead = Pressure Drop / (Density × Gravity)")
    print("=" * LINE_WIDTH)
    print(f"The pump head is: {pump_head:.2f} m")
    print("=" * LINE_WIDTH)
    return pump_head