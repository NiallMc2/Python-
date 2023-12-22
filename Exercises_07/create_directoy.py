import os, platform

# Define global variables
current_working_directory = None

def detect_os()->str:
    # Detect the OS in use
    return platform.system()

def detect_working_directory()->str:
    # Returns the directory this script was run from
    return os.getcwd()

if (__name__ == '__main__'):
    print(f"This module executes as a standalone script")
    
    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    
    # Parse the response, only check for Windows and Linux
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit()

    # Get the current working directory
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")

   

def create_directory(directory_name: str)->int: 
    # Check to see if the directory already exists
    if os.path.isdir(directory_name):
        # The directory already exists
        return 2
    else:
        # Use try/except to catch errors
        try:
            # Create the directory
            os.mkdir(directory_name)
            # If this worked, return True
            return 0
        except:
            # Give an explicit error message
            print(f"Error creating directory {directory_name}")
            # If this did not work, return False
            return 1
if create_directory("N") == 0:
        print("Creating a directory worked")
        # Do other stuff
elif create_directory("N") == 1:
        print("You couldn't create a directory!")
        # Do other stuff
elif create_directory("N") == 2:
        print("Directory already existed!")
        # Do other stuff
