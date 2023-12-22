""""
File utilities, forked from the Comm module of SD-Node, written c. 2017
Tested with Python >=3.6
By: JOR
    v0.1    26AUG21     
"""
from datetime import datetime as dt
import sys
import os

def path_name():
    # Operating system dependent stuff
    this_os = sys.platform
    if this_os == 'win32':
        return './Logfiles/'
    elif this_os == 'linux':
        return '/home/pi/Logfiles/'
    else:
        print(f'Unsupported OS: {this_os}')
        exit(0)

def log_file_name(client, file_extension=".csv"):
    """
    Create a file name in the logfiles directory, based on current data and time
    Requires the computer to have an RTC or synched clock
    """
    now = dt.now()
    # Linux
    file_name = f"UDP_Log{client}{file_extension}"
    return file_name

def create_log_file(log_path, filename, Data):
    full_path = os.path.join(log_path, filename)
    try:
        os.makedirs(log_path, exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(f"Log file created for {Data}\n")
        print(f"Log file '{filename}' created successfully at '{log_path}'")
    except IOError as e:
        print(f"Error creating log file: {e}")

if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
    log_path = path_name()
    filename = log_file_name("Client1")
    print(os.path.join(log_path, filename))
else:
    pass
    #print(f"This module is called {__name__} and is being called by another script")

