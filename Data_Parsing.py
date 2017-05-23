# file: Data_Parsing.py
# name: Steven Chen
# date: 09/19/2014
# mod : 09/22/2014

import csv
import os
import shutil
import time

#define the folder locations for the script
data_folder      = "/usr/local/smb-share/1.Projects/1.16.Kuykendall/data"
archive_folder   = "/usr/local/smb-share/1.Projects/1.16.Kuykendall/archive_raw"
processed_folder = "/usr/local/smb-share/1.Projects/1.16.Kuykendall/processed"


#target files within the data_folder directory
for target in os.listdir(data_folder):
    #target only CSV formatted files
    if target.endswith(".csv"):
        #form the path to th CSV file
        target_path = os.path.join(data_folder, target)
        #let user know which file is being processed
        print "Processing... " + target
        #open target in read only
        target_file = open(target_path, "r")
        #send target to csv reader for processing
        target_reader = csv.reader(target_file, delimiter = ",")
        #open a processed file
        processed_filename = os.path.splitext(target)[0] + "_processed" + \
                             os.path.splitext(target)[1]
        processed_path = os.path.join(processed_folder, processed_filename)
        processed_file = open(processed_path, "wb")
        processed_writer = csv.writer(processed_file)
        #read each row in the data file
        for row in target_reader:
            #check for dew point calculations
            if row[1].split("-")[1] == "x":
                #do not insert this row into the processed file
                pass
            #otherwise insert data into the processed file
            #remove '-' symbol from the sensor_sn
            else:
                processed_writer.writerow([row[0], row[1].split("-")[0] + \
                                           row[1].split("-")[1], row[2]])
        #close opened files to prevent memory leak
        target_file.close()
        processed_file.close()
        #archive raw data file
        shutil.move(target_path, archive_folder)
        #sleep for 5 seconds
        time.sleep(5)
        
