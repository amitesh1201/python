#!/usr/local/bin/python3.7


import os
from sys import exit
import csv
import fnmatch
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

host_name = 'localhost'
db_name = 'testdb'
user_name = 'postgres'
user_password = 'redhat'

#def connect_db():
#    conn = pg.connect(host='localhost', dbname='testdb', user='postgres', password='redhat')
#    show_databases(conn)

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
    user_password = input("Enter user password to connect: ")
    return user_password

#def connect_db(host_name,db_name,user_name,user_password):
def connect_db():
    # Connect the database
    
    host_name = get_hostname()
    db_name = get_dbname()
    user_name = get_username()
    user_password = get_password()

    conn = pg.connect(host=host_name, dbname=db_name, user=user_name, password=user_password)
    print ("Database connected")
    print("====================")
    return conn

def show_databases():
    # Return the connection of database and fetch records from the pg_catalog.pg_database table. 
    #conn = connect_db(host_name,db_name,user_name,user_password)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT datname FROM pg_catalog.pg_database')
    table_data = cur.fetchall()
    print("Database: ")
    # Display the data in single coloumn.
    for td in table_data:
        print(td[0])
    conn.close()
    #table_data = pd.read_sql('SELECT datname FROM pg_catalog.pg_database',conn)
    #table_data = pd.reconnect_db(host_name,db_name,user_name,user_password)ad_sql('SELECT datname FROM pg_catalog.pg_database',connect_db(host_name,db_name,user_name,user_password))
    #td = table_data.set_index("datname", drop = False)
    #print(table_data)
    #print(table_data.Name.to_string(index=False))


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
           

menu()         
#connect_db()
#connect_db(host_name,db_name,user_name,user_password)
#show_databases()

