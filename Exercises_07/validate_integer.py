from re import A

def validate_integer():
    # Loop forever
    while True:
        try:
            user_input = int(input("Enter an integer value: "))
        except:
            # Bad value, 
            print("Error")
            continue
        else:
            print("Valid input")
            # Good value, exit the loop
            break
        finally:
            # Continue
            print("This message shows every time, regardless of the programme flow")
    

validate_integer()

    

