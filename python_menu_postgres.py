#!/usr/local/bin/python3.7


import os
from sys import exit
import csv
import fnmatch
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine
import getpass

host_name = 'localhost'
db_name = 'testdb'
user_name = 'postgres'
user_password = 'redhat'

def get_hostname():
    host_name = input("Enter DB hostname to connect: ")  
    return host_name

def get_dbname():
    db_name = input("Enter database name to connect: ")
    return db_name

def get_username():
    user_name = input("Enter database username to connect: ")
    return user_name

def get_password():
    user_password = getpass.getpass("Enter user password to connect: ")
    return user_password

def get_list_dbs():
    db_sql_query = "SELECT datname FROM pg_catalog.pg_database" 
    return db_sql_query
  
def get_list_tables():
    table_sql_query = "SELECT table_name FROM information_schema.tables where table_schema='public'"  
    return table_sql_query

def get_sql_result(sql_query):
    # Return the connection of database and fetch records from the pg_catalog.pg_database table. 
    #conn = connect_db(host_name,db_name,user_name,user_password)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(sql_query)
    db_data = cur.fetchall()
    conn.close()
    return db_data

def connect_db():

    # Connect the database
    conn = pg.connect(host=host_name, dbname=db_name, user=user_name, password=user_password)
    print ("Database connected")
    print("====================")
    return conn

def show_databases():
    # Take input hostname, dbname, username and password from user
    host_name = get_hostname()
    db_name = get_dbname()
    user_name = get_username()
    user_password = get_password()

    db_data = get_sql_result(get_list_dbs()) 
    print("Databases: ")
    # Display the data in single coloumn.
    for td in db_data:
        print(td[0])

def show_tables():
    # Display the tables of selected database.
    
    flag = 0

    # If the entered database is not exist then exit the script.
    db_name = get_dbname()
    host_name = get_hostname()
    user_name = get_username()
    user_password = get_password()
    db_data = get_sql_result(get_list_dbs())
    for dbd in db_data:
        if dbd[0] == db_name:
            flag = 1
            break

    if flag == 0:
        print("The database", db_name, "not exist.Enter the valid database name")
        exit()
    
    # Display the table in single column
    table_data = get_sql_result(get_list_tables()) 
    for td in table_data:
        print(td[0])

    

def menu():
    # Display the database operations menu

    print ("This is menu function")

    menu_option = True
 

    while menu_option == True:
        print ("1. Show databases")
        print ("2. Show tables")
        print ("Option 3")
        
        opt = int(input("Select the option: "))
        
        if opt == 1:
           show_databases()
         
        if opt == 2:
           show_tables() 


        flag = input("Do you wish to continue: (y/n) ")

        if flag == "y":
           menu_option = True
        else:
           exit() 
           

######Main Section######
menu()         

