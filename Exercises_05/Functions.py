def function_test(Niall):
    """
    Simple test function
    """
    print(f"hello {Niall}!")

function_test("Niall")

def calculate_circumference(radius):
    """
    Calculate the circumference of a circle based on its radius
    """
    return 2 * 3.142 * radius 

a = calculate_circumference(5)
print(a)

def calculate_circumference(radius):
    """
    Calculate the circumference of a circle based on its radius

    """
    return 2 * 3.142 * radius 

# Get a radius value as a string
r = input("Provide a radius value: ")
# Convert it to a float
r_float = float(r)
# Call the function and create the variable for the return value
a = calculate_circumference(r_float)
print(a)
