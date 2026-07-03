from utils.geometry import calculate_pipe_area
from utils.validation import get_positive_float
from config import LINE_WIDTH

def pipe_velocity_calculator():
    print("\nPipe Velocity Calculator")
    flow_rate = get_positive_float("\nEnter the flow rate of the fluid (m^3/s): ")
    diameter = get_positive_float("\nEnter the diameter of the pipe (m): ")
    area = calculate_pipe_area(diameter)
    velocity = flow_rate / area
    print("=" * LINE_WIDTH)
    print(f"Pipe Area : {area:.6f} m²")
    print(f"The velocity of the fluid is: {velocity:.2f} m/s")
    print("=" * LINE_WIDTH)
    return velocity