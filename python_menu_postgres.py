#!/usr/local/bin/python3.7

:set number

import os
from sys import exit
import csv
import fnmatch
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

def connect_db(host_name,db_name,user_name,user_password):

    #conn = pg.connect(host='localhost', dbname=db_name, user='postgres', password='redhat')
    conn = pg.connect(host='$host_name', dbname=$db_name, user='$user_name', password='$user_password')

def show_databases():
    print("1. Show databases")


def menu():
    print ("This is menu function")

    menu_option = True
 

    while menu_option == True:
        print ("1. Show databases")
        print ("Option 2")
        print ("Option 3")

        opt = int(input("Select the option: "))
        
        if opt == 1:
            show_databases() 

        flag = input("Do you wish to continue: (y/n) ")

        if flag == "y":
           menu_option = True
        else:
           exit() 
           

#menu()         
connect_db


