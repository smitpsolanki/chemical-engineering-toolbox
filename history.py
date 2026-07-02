from config import LINE_WIDTH


history = []

def add_history(calculator, result):
    history.append(
        {
            "calculator": calculator,
            "result": result
        }
    )
def show_history():
    if not history:
        print("\nNo history available.")
        return
    print("=" * LINE_WIDTH)
    print("Calculation History.".center(LINE_WIDTH))
    print("=" * LINE_WIDTH)
    for number, entry in enumerate(history, start=1):
        print(f"Calculation #{number}")
        print("-" * LINE_WIDTH)
        print(f"Calculator : {entry['calculator']}")
        print(f"Result     : {entry['result']}")
        print()
def clear_history():
    if not history:
        print("\nNo history available to clear.")
        return
    history.clear()
    print("\nHistory cleared successfully.")