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
    print("\nCalculation History")
    print("=" * 40)
    for entry in history:
        print("-" * 40)
        print(f"Calculator : {entry['calculator']}")
        print(f"Result     : {entry['result']}")
        print()
