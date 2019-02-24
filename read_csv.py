#!/usr/bin/python

import csv
import os
import fnmatch
from collections import defaultdict

columns = defaultdict(list)
file_name = input("Eneter filename: ")
if (os.path.isfile(file_name.strip())):
    print(file_name, "exist")
    if fnmatch.fnmatch(file_name,'*.csv'):
        print(file_name)
        with open(file_name,'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for (i,v) in enumerate(row):
                    columns[i].append(v)
                #print (row)
        print(columns[0])        
        #print(columns[4])        
       # print(columns[9])        
        csvfile.close()        
    else:
        print(file_name,"not csv")
else: 
    print(file_name, "not exist")
