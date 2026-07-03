from config import LINE_WIDTH
from datetime import datetime


history = []

def add_history(calculator, result):
    now = datetime.now()
    history.append(
        {   
            "date": now.strftime("%d-%m-%Y"),
            "time": now.strftime("%I:%M %p"),
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
        print(f"Date       : {entry['date']}")
        print(f"Time       : {entry['time']}")
        print(f"Calculator : {entry['calculator']}")
        print(f"Result     : {entry['result']}")
        print()
def clear_history():
    if not history:
        print("\nNo history available to clear.")
        return
    history.clear()
    print("\nHistory cleared successfully.")
def save_history(): 
    with open("history.csv", "w") as file:
        file.write("Date,Time,Calculator,Result\n")
        for entry in history:
            line = f"{entry['date']},{entry['time']},{entry['calculator']},{entry['result']}\n"
            file.write(line)
    print("\nHistory saved successfully.")
def load_history():
    try:
        with open("history.csv", "r") as file:
            next(file)
            for line in file:
                parts=line.strip().split(",")
                history.append(
                    {
                        "date": parts[0],
                        "time": parts[1],
                        "calculator": parts[2],
                        "result": parts[3]
                    }
                )
    except FileNotFoundError:
        return