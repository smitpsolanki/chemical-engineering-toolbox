from utils.input_helpers import get_float, select_option
from utils.units import convert_density, convert_length, convert_velocity, convert_viscosity
from utils.validation import get_positive_float
FLUIDS = {
        "1": {
            "name": "water",
            "density": 1000,
            "viscosity": 0.001
        },
        "2": {
            "name": "air",
            "density": 1.225,
            "viscosity": 0.000018
        },
        "3": {
            "name": "oil",
            "density": 850,
            "viscosity": 0.1
        }
    }
def reynolds_calculator():
    print("\nReynolds Number Calculator")
    print("1. Water\n2. Air\n3. Oil\n4. Custom Fluid")
    fluid=input("\nEnter the fluid name (1-4): ").lower().strip()
    if fluid in FLUIDS:
        selected=FLUIDS[fluid]
        name=selected["name"]
        density=selected["density"]
        viscosity=selected["viscosity"]
    elif fluid == "4":
        name="Custom Fluid"
        try:
            density=get_positive_float("Enter the density of the fluid: ")
            density_unit=select_option("Select the unit for density:", ["kg/m3", "g/cm3", "lb/ft3"])
            density=convert_density(density, density_unit)
            viscosity=get_positive_float("Enter the viscosity of the fluid (Pa·s): ")
            viscosity_unit=select_option("Select the unit for viscosity:", ["Pa·s", "cP"])
            viscosity=convert_viscosity(viscosity, viscosity_unit)
        except ValueError:
            print("\nInvalid input. Please enter numeric values.")
            return
    else:
        print("Invalid fluid name. Please enter '1', '2', '3', or '4'.")
        return     
    print("\nSelected fluid:", name)
    print(f"\nDensity: {density} kg/m^3")
    print(f"\nViscosity: {viscosity} Pa·s")
    diameter=get_positive_float("\nEnter the diameter of the pipe (m): ")
    diameter_unit=select_option("Select the unit for diameter:", ["m", "cm", "mm", "in", "ft"])
    diameter=convert_length(diameter, diameter_unit)
    velocity=get_positive_float("\nEnter the velocity of the fluid (m/s): ")
    velocity_unit=select_option("Select the unit for velocity:", ["m/s", "cm/s", "mm/s", "in/s", "ft/s"])
    velocity=convert_velocity(velocity, velocity_unit)
    reynolds_number=(density*velocity*diameter)/viscosity
    print(f"\nThe Reynolds number is: {reynolds_number:.2f}")
    if reynolds_number < 2000:
        print("The flow is laminar.")  
    elif reynolds_number < 4000:
        print("The flow is transitional.")
    else:
        print("The flow is turbulent.")
    
    return reynolds_number