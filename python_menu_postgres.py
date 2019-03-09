#!/usr/local/bin/python3.7

import os
from sys import exit
import csv
import fnmatch
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

def show_databases():
    print("1. Show databases")


def menu():
    print ("This is menu function")

    menu_option = True
 

    while menu_option == True:
        print ("1. Show databases")
        print ("Option 2")
        print ("Option 3")

        opt = input("Select the option: ")
        
        if opt == 1:
            show_databases() 

        flag = input("Do you wish to continue: (y/n) ")

        if flag == "y":
           menu_option = True
        else:
           exit() 
           

menu()         

