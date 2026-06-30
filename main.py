from calculators.reynolds import reynolds_calculator
from calculators.pump_head import pump_calculator
while True:
    print("=" * 40)
    print("Welcome to the Chemical Engineering Toolbox")
    print("=" * 40)
    choice = input("\nSelect a calculator:\n1. Reynolds Number Calculator\n2. Pump Head Calculator\n\nEnter your choice (1 or 2): ").strip().lower()
    match choice:
        case "1":
            reynolds_calculator()  
        case "2":
            pump_calculator()
        case _:
            print("\nInvalid choice. Please enter '1' or '2'.")
            continue
    repeat = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
    if repeat != "y":
        print("\nThank you for using the Chemical Engineering Toolbox. Goodbye!\n")
        break
