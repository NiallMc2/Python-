'''
Main by: NMG
Creating a server that takes information from UDP client information from os_utilities.py and creates log files for those details
Server settings are imported from mypaths as a method to send temperature warning notifications
Alpha: 10 NOV 23
'''

from time import sleep # importing sleep function from time so logs can be saved in a specified timeframe
from Source.file_utilities import path_name, log_file_name # importing path_name and log_file_name from module Source.file_utilites
from Source.os_utilities import detect_os, Rasp_Pi1, Rasp_Pi2, Rasp_Pi3 #importing configuration details from module Source.os_utilites
from Source.logfile_utilites import file_folder #importing file folder from module Source.logfile_utilities
from mypaths import UDP_SETTINGS as Server_IP # Parent directory changed in mypaths and server IP address imported


# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".csv")


# Loop forever
while True:
    # Sleep for 1 second
    sleep(1)
    # Get a time stamp for this line
    timestamp = log_file_name("")

    # Get information from all UDP clients, imported from os_utilities
    info1 = Rasp_Pi1()
    info2 = Rasp_Pi2()
    info3 = Rasp_Pi3()


    # Creating log entries with respective client file names by concatenating the information (log_file_name, unique sensor id, sensor name, time, temp) imported from os_utilities. 
    # Server_IP is imported from mypaths.py. 
    # using f-string literals to extract the information


    logline1 = f"{timestamp} - Rasp Pi1 - Log_ID1: {info1.get('ID1', '')}, Time: {info1.get('Time', '')}, Name: {info1.get('Name', '')}, Temp: {info1.get('Temp', '')} Server: {Server_IP},\n"
    logline2 = f"{timestamp} - Rasp Pi2 - Log_ID2: {info2.get('ID2', '')}, Time: {info2.get('Time', '')}, Name: {info2.get('Name', '')}, Temp: {info2.get('Temp', '')} Server: {Server_IP},\n"
    logline3 = f"{timestamp} - Rasp Pi3 - Log_ID3: {info3.get('ID3', '')}, Time: {info3.get('Time', '')}, Name: {info3.get('Name', '')}, Temp: {info3.get('Temp', '')} Server: {Server_IP},\n"

    # Write to log files(UDP_ID is contained within)
    try:
        #creating iterable sequece for 3 client between 1 to 4 excluding 4
        for UDP_ID, logline in zip(range(1, 4), [logline1, logline2, logline3]):
            filename = log_file_name(UDP_ID)
            full_path = file_folder(log_path, filename)
            
            #appending new data to the existing files
            with open(full_path, "a") as file_handle:
                print(f"logging to {full_path}")
                file_handle.write(logline)
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    except OSError:
        print("OS Error")
    except Exception as e:
        print(f"General Error: {e}")