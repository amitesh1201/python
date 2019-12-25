#!/usr/bin/python

# This script display files on user enter path and date.
import os, sys, datetime

list_month_31=[1,3,5,7,8,10,12]
list_month_30=[4,6,9,11]
leap_month_year=2
flag=0
lst_exit_file_date=[]

dir_path=input("Enter the directoy path: ")

if not dir_path:
    print("The directory should not be empty. Re-run the script and enter the valid directory path.")
    sys.exit(1)

cdate=input("Enter creation date of the file in the yyy-mm-dd formate: ")

if not cdate:
    print("The creation date of file should not be empty. Re-run the script and enter the valid creation date in the yyy-mm-dd formate.")
    sys.exit(1)


lst_year=cdate.split('-')[0]
lst_month=cdate.split('-')[1]
lst_days=cdate.split('-')[2]

if not "-" in cdate:
    print("Enter the valid date formate: yyyy-mm-dd")
    sys.exit(1)

if len(lst_year) != 4:
    print("Enter the valid date formate: yyyy-mm-dd")
    sys.exit(1)

if len(lst_month) > 2:
    print("Enter the valid date formate: yyyy-mm-dd")
    sys.exit(1)

lst_int_month=int(lst_month)
if lst_int_month > 12:
    print("Entered month should not be greater than 12")
    sys.exit(1)

if (lst_int_month in list_month_30 or int(lst_month) == leap_month_year) and (int(lst_days) == 31):
    print(f"Entered {lst_month} is of 30 days")
    sys.exit(1)

lst_int_year=int(lst_year)
if (lst_int_year % 4) == 0 and (lst_int_year % 100) == 0 and (lst_int_year % 400) == 0 and int(lst_days) >= 29:
    print("Entered year is leap year and days are 28")
    sys.exit(1)

if int(lst_month) == 2 and int(lst_days) >= 30:
    print("Enter month is 28 or 29 days")
    sys.exit(1)

if len(lst_days) != 2:
    print("Enter the valid date formate: yyyy-mm-dd")
    sys.exit(1)

if int(lst_days) > 31:
    print("Enter days should not be greate than 31")
    sys.exit(1)

if not os.path.exists(dir_path):
    print("Enter valid dir path: ")
    sys.exit(1)
    
lst_dir=os.listdir(dir_path)    

for each_file in range(len(lst_dir)):
    file_exist=os.path.join(dir_path,lst_dir[each_file])
    if os.path.isfile(file_exist):
         file_cdate=datetime.datetime.fromtimestamp(os.path.getctime(file_exist)).strftime("%Y-%m-%d")
         if cdate == file_cdate:
             lst_exit_file_date.append(file_exist)
#           print(file_exist)
             
if len(lst_exit_file_date) != 0:
    print(f"The following files are created on date {cdate}:")
    for each_file_exist in lst_exit_file_date:
        print(f"{each_file_exist}")
else:
    print(f"The files are not found on date {cdate}")
