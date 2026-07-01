from history import add_history, show_history
from calculators.reynolds import reynolds_calculator
from calculators.pump_head import pump_calculator
while True:
    print("=" * 60)
    print("Welcome to my Chemical Engineering Toolbox")
    print("=" * 60)
    choice = input("\nSelect a calculator:\n1. Reynolds Number Calculator\n2. Pump Head Calculator\n3. Show History\n4. Exit\n\nEnter your choice (1-4): ").strip().lower()
    match choice:
        case "1":
            result=reynolds_calculator()
            add_history("Reynolds Number Calculator", result)
        case "2":
            result=pump_calculator()
            add_history("Pump Head Calculator", result)
        case "3":
            show_history()
        case "4":
            print("\nThank you for using the Chemical Engineering Toolbox. Goodbye!\n")
            break
        case _:
            print("\nInvalid choice. Please enter '1', '2', '3', or '4'.")
            continue
