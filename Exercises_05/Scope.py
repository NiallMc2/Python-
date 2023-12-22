my_string = "global"

def my_function():
    my_string = "enclosing"
    def nested_function():
        my_string = "local"
        print(my_string)
    nested_function()
    return my_string

# Print the variable my_string
print(my_string)
# Print the output of the function, my_function
print(my_function())

def divisible(numerator: int, denominator: int)->bool:
    return numerator % denominator == 0

print(divisible(30,5))

# because 30/5 is divisible = 6