from config import LINE_WIDTH
from resources.fluid_mechanics.pump_head import COMMON_MISTAKES, ENGINEERING_TIP, FORMULA, INDUSTRIAL_APPLICATIONS, INTERPRETATION
from utils.formatter import print_footer, print_header, print_paragraph, print_result, print_section
from utils.input_helpers import get_float
from utils.units import convert_density, convert_pressure
from utils.validation import get_positive_float
from utils.input_helpers import select_option
def pump_calculator():
    print_header("Pump Head Calculator")
    pressure_drop = get_positive_float("\nEnter the pressure drop across the pump: ")
    pressure_unit = select_option("Select the unit for pressure drop:", ["Pa", "kPa", "MPa", "bar", "psi"])
    pressure_drop = convert_pressure(pressure_drop, pressure_unit)
    density = get_positive_float("\nEnter the density of the fluid: ")
    density_unit = select_option("Select the unit for density:", ["kg/m3", "g/cm3", "lb/ft3"])
    density = convert_density(density, density_unit)
    pump_head = pressure_drop / (density * 9.81)
    print_header("Results")
    print_result("\nPump Head", pump_head, "m")
    print_result("\nFormula", FORMULA)
    print_section("\nInterpretation")
    print_paragraph(INTERPRETATION)
    print_section("\nEngineering Tip")
    print_paragraph(ENGINEERING_TIP)
    print_section("\nIndustrial Applications")
    print_paragraph(INDUSTRIAL_APPLICATIONS)
    print_section("\nCommon Mistakes")
    print_paragraph(COMMON_MISTAKES)
    print_footer()
    return pump_head