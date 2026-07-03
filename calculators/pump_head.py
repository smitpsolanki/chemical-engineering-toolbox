from config import LINE_WIDTH
from utils.input_helpers import get_float
from utils.validation import get_positive_float
def pump_calculator():
    print("\nPump Head Calculator")
    pressure_drop = get_positive_float("\nEnter the pressure drop across the pump (Pa): ")
    density = get_positive_float("\nEnter the density of the fluid (kg/m^3): ")
    pump_head = pressure_drop / (density * 9.81)
    print("\nUsing equation:")
    print("\nHead = Pressure Drop / (Density × Gravity)")
    print("=" * LINE_WIDTH)
    print(f"The pump head is: {pump_head:.2f} m")
    print("=" * LINE_WIDTH)
    return pump_head