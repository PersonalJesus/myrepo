#!/bin/python3


from fileinput import filename
import shutil       #For Copy_file
import os           #For Get_file_size and Chech_if_file_exist
import sys          #For CLI_arguments

# How to execute script:: ./Purgelog.py Logexample.txt 10 5
# Where:
# Purgerlog.py   - script name
# Logexample.txt - log file name
# 10             - file size oin kb
# 5              - numbers of file


if len(sys.argv) < 4:
    print("Missing arguments!")
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_numbers = int(sys.argv[3])

if os.path.isfile(file_name) == True:         # Check if file exist
    logfile_size = os.stat(file_name).st_size   # Get file size in bytes
    logfile_size = logfile_size / 1024          # Convert bytes to kb

    if logfile_size >= limit_size:
        if logs_numbers > 0:
            for current_file_num in range(logs_numbers, 1, -1):
                src = file_name + "_" + str(current_file_num-1)
                dst = file_name + "_" + str(current_file_num)
                if os.path.isfile(src) == True:
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + " to " + file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()