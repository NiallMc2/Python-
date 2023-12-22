""""
OS utilities
Tested with Python >=3.6
By: JOR
    v0.1    26AUG21     
"""
import platform
from datetime import datetime
import uuid


def detect_os()->str:
    # Detect the OS in use
    return platform.system()

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    
    # Parse the response
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your Apple system is MacOS")
    elif my_os == "cygwin":
        print("Your Apple system is MacOS")
    elif my_os == "aix":
        print("Your IBM system is AIX")
    else:
        print(f"Unidentified system = {my_os}")
else:
    pass
    #print(f"This module is called {__name__} and is being called by another script")



def Rasp_Pi1():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Log_ID1= uuid.uuid4().hex[:4]  # creating a unique log id 4 digits long
    data1 = {
        "Time": current_datetime,
        "Name": "Tempsense1",
        "Temperature": "20 C",
        "ID1": Log_ID1
        
    }
    return data1



def Rasp_Pi2():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Log_ID2= uuid.uuid4().hex[:4]  # creating a unique log id 4 digits long
    data2 = {
        "Time": current_datetime,
        "Name": "Tempsense2",
        "Temperature": "20 C",
        "ID2": Log_ID2
        
    }
    return data2


def Rasp_Pi3():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Log_ID3= uuid.uuid4().hex[:4]  # creating a unique log id 4 digits long
    data3 = {
        "Time": current_datetime,
        "Name": "Tempsense3",
        "Temperature": "20 C",
        "ID3": Log_ID3
        
    }
    return data3

