from utils.input_helpers import get_float, select_option
from utils.units import convert_density, convert_length, convert_velocity, convert_viscosity
from utils.validation import get_positive_float
from utils.formatter import print_footer, print_header, print_paragraph, print_result, print_section
from resources.dimensionless_numbers.reynolds import (LAMINAR_LIMIT, TRANSITION_LIMIT, FORMULA, FLOW_REGIMES)
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
    print_header("Reynolds Number Calculator")
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
            viscosity=get_positive_float("Enter the viscosity of the fluid: ")
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
    diameter=get_positive_float("\nEnter the diameter of the pipe: ")
    diameter_unit=select_option("Select the unit for diameter:", ["m", "cm", "mm", "in", "ft"])
    diameter=convert_length(diameter, diameter_unit)
    velocity=get_positive_float("\nEnter the velocity of the fluid: ")
    velocity_unit=select_option("Select the unit for velocity:", ["m/s", "cm/s", "mm/s", "in/s", "ft/s"])
    velocity=convert_velocity(velocity, velocity_unit)
    reynolds_number=(density*velocity*diameter)/viscosity
    print_header("Results")
    print_result("\nReynolds Number", reynolds_number)
    if reynolds_number < LAMINAR_LIMIT:
        flow_regime = "Laminar"
        print_result("\nFlow Regime", flow_regime)
        print_result("\nFormula", FORMULA)
        print_section("\nInterpretation")
        print_paragraph(FLOW_REGIMES[flow_regime]["interpretation"])
        print_section("\nTip")
        print_paragraph(FLOW_REGIMES[flow_regime]["tip"])
        print_footer()
    elif reynolds_number < TRANSITION_LIMIT:
        flow_regime = "Transition"
        print_result("\nFlow Regime", flow_regime)
        print_result("\nFormula", FORMULA)
        print_section("\nInterpretation")
        print_paragraph(FLOW_REGIMES[flow_regime]["interpretation"])
        print_section("\nTip")
        print_paragraph(FLOW_REGIMES[flow_regime]["tip"])  
        print_footer()
    else:
        flow_regime = "Turbulent"
        print_result("\nFlow Regime", flow_regime)
        print_result("\nFormula", FORMULA)
        print_section("\nInterpretation")
        print_paragraph(FLOW_REGIMES[flow_regime]["interpretation"])
        print_section("\nTip")
        print_paragraph(FLOW_REGIMES[flow_regime]["tip"])
        print_footer()
    return reynolds_number