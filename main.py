from history import add_history, show_history, clear_history
from calculators.reynolds import reynolds_calculator
from calculators.pump_head import pump_calculator
from config import APP_NAME, VERSION, AUTHOR, LINE_WIDTH
while True:
    print("=" * LINE_WIDTH)
    print(APP_NAME.center(LINE_WIDTH))
    print(f"Version: {VERSION}".center(LINE_WIDTH))
    print(f"Developed by: {AUTHOR}".center(LINE_WIDTH))
    print("=" * LINE_WIDTH)
    choice = input("\nSelect a calculator:\n1. Reynolds Number Calculator\n2. Pump Head Calculator\n3. Show History\n4. Clear History\n5. Exit\n\nEnter your choice (1-5): ").strip().lower()
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
            if input("\nAre you sure you want to clear the history? (y/n): ").strip().lower() == 'y':
                clear_history()
            else:
                print("\nHistory not cleared.")
        case "5":
            print("\nThank you for using the Chemical Engineering Toolbox. Goodbye!\n")
            break
        case _:
            print("\nInvalid choice. Please enter '1', '2', '3', '4', or '5'.")
            continue
