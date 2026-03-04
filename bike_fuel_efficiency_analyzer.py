# Bike fuel efficiency and cost running cost analyzer
# Created by Vaibhav Kale
# Date: 5 Mar 2026


print("======== BIKE FUEL EFFICIENCY AND RUNNING COST ANALYZER ========")

print("\n\nWelcome to Bike Fuel Efficiency and Running Cost Analyzer!")
print("Enter the correct details for the following fields:-")
print("\n- Total distance travelled (in km)")
print("- Total fuel used (in liters)")
print("- Total fuel price per liter (in rupees)")
print("- Engine power (in cc)")

print("\nNOTE:-")
print("\n# Provided information must not be negative or zero")
print("# Provided information must not be fractional like 3/4, 5/4 etc")
print("# Provided information must not be alphabets or special characters")
print("# All fields are mandatory\n")

# User Inputs
print("Enter Details Below:-")

dt = float(input("\nTotal distance travelled (in km) : "))
fu = float(input("Total fuel used (in liters) : "))
fp = float(input("Total fuel price per liter (in rupees) : "))
ep = float(input("Engine power (in cc) : "))

print("\n================== BIKE FUEL ANALYSIS REPORT ==================")

if dt <= 0 or fu <= 0 or fp <= 0 or ep <= 0:
    print("\nThe provided input values are invalid, please try again...")
else:
    # Calculations
    m = dt / fu                      # Mileage km/l
    cpkm = (fp*fu) / dt        # Cost per km
    tfc = fu * fp                    # Total fuel cost

    print("\nMILEAGE :", round(m, 2), "km/l")
    print("\nFUEL COST PER KM :", "₹", round(cpkm, 2))
    print("\nTOTAL FUEL COST :", "₹", round(tfc, 2))

    # Determine bike type and expected mileage
    if ep <= 80:
        bike = "Moped"
        exmile = (65, 75)
        speed = (35, 45)
    
    elif ep <= 125:
        bike = "Commuter Motorcycle"
        exmile = (50, 65)
        speed = (40, 55)
    
    elif ep <= 220:
        bike = "Premium Commuter Motorcycle"
        exmile = (35, 50)
        speed = (50, 65)
    
    elif ep <= 450:
        bike = "Performance Motorcycle"
        exmile = (25, 35)
        speed = (60, 75)
    
    elif ep <= 650:
        bike = "High-Performance Motorcycle"
        exmile = (15, 25)
        speed = (70, 90)
    
    elif ep <= 1000:
        bike = "Superbike"
        exmile = (10, 20)
        speed = (80, 100)
    
    elif ep <= 1500:
        bike = "Premium Superbike"
        exmile = (8, 15)
        speed = (85, 105)
    
    elif ep <= 2000:
        bike = "Hyperbike"
        exmile = (6, 12)
        speed = (90, 110)
    
    else:
        bike = "Premium Hyperbike"
        exmile = (5, 10)
        speed = (95, 115)

    print("\nYOUR BIKE TYPE :", bike)
    print("\nEXPECTED IDEAL MILEAGE RANGE :", exmile[0], "-", exmile[1], "km/l")

    # Compare mileage with expected range
    if m < exmile[0]:
        efficiency_status = "Below expected - maintenance suggested"
        maintenance = "Consider servicing."
    
    elif m > exmile[1]:
        efficiency_status = "Above expected"
        maintenance = "Mileage unusually high"
    
    else:
        efficiency_status = "Within expected range - bike is fine"
        maintenance = "No immediate maintenance needed."

    print("\nEFFICIENCY STATUS :", efficiency_status)
    print("\nMAINTENANCE SUGGESTION :", maintenance)
    print("\nBEST SPEED FOR MAXIMUM EFFICIENCY :", speed[0], "-", speed[1], "km/h")
    
print("\n========================== RIDE SAFE ==========================")