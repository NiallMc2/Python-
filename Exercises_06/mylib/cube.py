cube_text = "Yo, time to cube stuff!"

def cube(x):
    return x*x*x

# Uncomment to test
#print(cube(2))

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    print(cube(2))
    
else:
    print(f"This module is called {__name__} and is being called by another script")