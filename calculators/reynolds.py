def reynolds_calculator():
    print("\nReynolds Number Calculator")
    print("1. Water\n2. Air\n3. Oil\n4. Custom Fluid")
    fluid=input("\nEnter the fluid name (1-4): ").lower().strip()
    match fluid:
        case "1":
            density=1000
            viscosity=0.001 
        case "2":
            density=1.225
            viscosity=0.000018
        case "3":
            density=850
            viscosity=0.1
        case "4":
            density=float(input("Enter the density of the fluid (kg/m^3): "))
            viscosity=float(input("Enter the viscosity of the fluid (Pa·s): "))
        case _:
            print("Invalid fluid name. Please enter '1', '2', '3', or '4'.")
            return
    if fluid == "1":
        fluid = "water"
    elif fluid == "2":      
        fluid = "air"
    elif fluid == "3":
        fluid = "oil" 
    else:
        fluid = "custom fluid"      
    print(f"\nSelected Fluid: {fluid.capitalize()}")
    print(f"\nDensity: {density} kg/m^3")
    print(f"\nViscosity: {viscosity} Pa·s")
    diameter=float(input("\nEnter the diameter of the pipe (m): "))
    velocity=float(input("\nEnter the velocity of the fluid (m/s): "))
    reynolds_number=(density*velocity*diameter)/viscosity
    print(f"\nThe Reynolds number is: {reynolds_number:.2f}")
    if reynolds_number < 2000:
        print("The flow is laminar.")  
    elif reynolds_number < 4000:
        print("The flow is transitional.")
    else:
        print("The flow is turbulent.")