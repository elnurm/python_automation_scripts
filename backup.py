#!/usr/bin/env python
 
# script for back up yesterdays log files to a shared folder
# dest_path "/backup/" cifs mounted folder to centos

import os
import shutil
from datetime import date, time, datetime, timedelta
 
yesterday = date.today() - timedelta(1)
yesterday = str(yesterday)
 
dest_path = "/backup/" + yesterday
print "Destination path is : " + dest_path
source_path = "/some/path/"
print "Source path is : " + source_path
try:
    os.mkdir(dest_path)
    print "The %s directory was created!" % dest_path
except OSError:
    print "Failed to create the directory %s , seems it's already created manually" % dest_path
 
files = os.listdir(source_path)
total_copied_files = 0
print "Script is starting to copy the files..."
for file in files:
    try:
        file_stat = os.stat("/some/path/" + str(file))
        mod_time = datetime.fromtimestamp(file_stat.st_mtime)
        if mod_time.date() == datetime.now().date() - timedelta(1):
            shutil.copy(source_path+str(file),dest_path)
            print file + " copied" + " Modification Time : " + str(mod_time.date())
            total_copied_files += 1
    except OSError:
        continue
 
print "Total " + str(total_copied_files) + " files copied."
