from utils.validation import get_positive_integer


def get_float(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
def select_option(title,options):
    print(f"\n{title}")
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")
    while True:
        choice = get_positive_integer("Enter your choice: ")
        if 1 <= choice <= len(options):
            return options[choice - 1]
        else:
            print(f"Please enter a number between 1 and {len(options)}.")