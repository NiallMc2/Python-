"""
create_logfile.py
By: NMG
Date: 10 NOV 23
Taken from  Exercises_07 file_handler.py
"""


import os

def file_folder(log_path, filename):
    data_folder = os.path.join(log_path, 'data')
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    return os.path.join(data_folder, filename)
