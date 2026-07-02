from utils.input_helpers import get_float
def pump_calculator():
    print("\nPump Head Calculator")
    pressure_drop = get_float("\nEnter the pressure drop across the pump (Pa): ")
    density = get_float("\nEnter the density of the fluid (kg/m^3): ")
    pump_head = pressure_drop / (density * 9.81)
    print("\nUsing equation:")
    print("\nHead = Pressure Drop / (Density × Gravity)")
    print("=" * 40)
    print(f"The pump head is: {pump_head:.2f} m")
    print("=" * 40)
    return pump_head