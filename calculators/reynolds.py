from utils.input_helpers import get_float
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
            density=get_float("Enter the density of the fluid (kg/m^3): ")
            viscosity=get_float("Enter the viscosity of the fluid (Pa·s): ")
        except ValueError:
            print("\nInvalid input. Please enter numeric values.")
            return
    else:
        print("Invalid fluid name. Please enter '1', '2', '3', or '4'.")
        return     
    print("\nSelected fluid:", name)
    print(f"\nDensity: {density} kg/m^3")
    print(f"\nViscosity: {viscosity} Pa·s")
    diameter=get_float("\nEnter the diameter of the pipe (m): ")
    velocity=get_float("\nEnter the velocity of the fluid (m/s): ")
    reynolds_number=(density*velocity*diameter)/viscosity
    print(f"\nThe Reynolds number is: {reynolds_number:.2f}")
    if reynolds_number < 2000:
        print("The flow is laminar.")  
    elif reynolds_number < 4000:
        print("The flow is transitional.")
    else:
        print("The flow is turbulent.")