def get_positive_float(prompt):
    while True:
        try:
            value=float(input(prompt))
            if value <= 0:
               print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
def get_positive_integer(prompt):
    while True:
        try:
            value=int(input(prompt))
            if value <= 0:
               print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")