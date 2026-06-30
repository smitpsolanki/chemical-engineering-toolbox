fluid=input("\nEnter the fluid name(water/air/oil/custom):").lower().strip()
match fluid:
    case "water":
        density=1000
        viscosity=0.001 
    case "air":
        density=1.225
        viscosity=0.000018
    case "oil":
        density=850
        viscosity=0.1
    case "custom":
        density=float(input("Enter the density of the fluid (kg/m^3): "))
        viscosity=float(input("Enter the viscosity of the fluid (Pa·s): "))
    case _:
        print("Invalid fluid name. Please enter 'water', 'air', 'oil', or 'custom'.")
        exit()
diameter=float(input("Enter the diameter of the pipe (m): "))
velocity=float(input("Enter the velocity of the fluid (m/s): "))
reynolds_number=(density*velocity*diameter)/viscosity
print(f"\nThe Reynolds number is: {reynolds_number:.2f}")
if reynolds_number < 2000:
    print("The flow is laminar.")  
elif reynolds_number < 4000:
    print("The flow is transitional.")
else:
    print("The flow is turbulent.") 