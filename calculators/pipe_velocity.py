from utils.geometry import calculate_pipe_area
from utils.input_helpers import select_option
from utils.units import convert_flow_rate, convert_length
from utils.validation import get_positive_float
from config import LINE_WIDTH

def pipe_velocity_calculator():
    print("\nPipe Velocity Calculator")
    flow_rate = get_positive_float("\nEnter the flow rate of the fluid: ")
    flow_unit = select_option("Select the unit for flow rate:", ["m³/s", "m³/hr", "L/s", "L/min"])
    flow_rate = convert_flow_rate(flow_rate, flow_unit)
    diameter = get_positive_float("\nEnter the diameter of the pipe: ")
    diameter_unit = select_option("Select the unit for diameter:", ["m", "cm", "mm", "in", "ft"])
    diameter = convert_length(diameter, diameter_unit)
    area = calculate_pipe_area(diameter)
    velocity = flow_rate / area
    print("=" * LINE_WIDTH)
    print(f"Pipe Area : {area:.6f} m²")
    print(f"The velocity of the fluid is: {velocity:.2f} m/s")
    print("=" * LINE_WIDTH)
    return velocity