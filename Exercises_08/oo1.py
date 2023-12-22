"""
Simple Class by NMG, by convention, use camel case to name classes
"""

# Create a class 
class NMGsClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for NMGsClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = NMGsClass("Morning NMG!")
my_class1.my_method()
my_class2 = NMGsClass("Morning NMG!")
my_class2.my_method()
print(type(my_class1))
print(type(my_class2))