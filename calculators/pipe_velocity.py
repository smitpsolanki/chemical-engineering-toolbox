from resources.fluid_mechanics.pipe_velocity import COMMON_MISTAKES, ENGINEERING_TIP, FORMULA, INDUSTRIAL_APPLICATIONS, INTERPRETATION, TYPICAL_RANGES
from utils.formatter import print_footer, print_header, print_paragraph, print_result, print_section, print_dictionary
from utils.geometry import calculate_pipe_area
from utils.input_helpers import select_option
from utils.units import convert_flow_rate, convert_length
from utils.validation import get_positive_float
from config import LINE_WIDTH

def pipe_velocity_calculator():
    print_header("Pipe Velocity Calculator")
    flow_rate = get_positive_float("\nEnter the flow rate of the fluid: ")
    flow_unit = select_option("Select the unit for flow rate:", ["m³/s", "m³/hr", "L/s", "L/min"])
    flow_rate = convert_flow_rate(flow_rate, flow_unit)
    diameter = get_positive_float("\nEnter the diameter of the pipe: ")
    diameter_unit = select_option("Select the unit for diameter:", ["m", "cm", "mm", "in", "ft"])
    diameter = convert_length(diameter, diameter_unit)
    area = calculate_pipe_area(diameter)
    velocity = flow_rate / area
    print_header("Results")
    print_result("\nPipe Velocity", velocity, "m/s")
    print_result("\nFormula", FORMULA)
    print_section("\nInterpretation")
    print_paragraph(INTERPRETATION)
    print_section("\nEngineering Tip")
    print_paragraph(ENGINEERING_TIP)
    print_section("\nTypical Ranges")
    print_dictionary(TYPICAL_RANGES)
    print_section("\nIndustrial Applications")
    print_paragraph(INDUSTRIAL_APPLICATIONS)
    print_section("\nCommon Mistakes")
    print_paragraph(COMMON_MISTAKES)
    print_footer()
    return velocity