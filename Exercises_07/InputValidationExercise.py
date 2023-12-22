def endurance_calc():
    # Fuel Amount
    while True:
        try:
            fuel = int(input("Enter fuel amount in litres: "))
        except:
            # Bad value, 
            print("Error")
            continue
        else:
            print("Valid input")
            # Good value, exit the loop
            break
        

    # Fuel Consumption
    while True:
        try:
            consumption = int(input("Enter consumption amount in litres per minute: "))
        except:
            # Bad value, 
            print("Error")
            continue
            
        else:
            print("Valid input")
            # Good value, exit the loop
            break
        

    # Calculate remaining endurance
    try:
        remaining_endurance = fuel / consumption
    except ZeroDivisionError:
        print("Fuel consumption is zero; cannot calculate")
        

    return remaining_endurance

remaining_endurance = endurance_calc()

print(f"Remaining Endurance: {remaining_endurance} minutes")






    

    