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

def connect_db(host_name,db_name,user_name,user_password):
    # Connect the database
    conn = pg.connect(host=host_name, dbname=db_name, user=user_name, password=user_password)
    print ("Database connected")
    print("====================")
    return conn

def show_databases():
     
    conn = connect_db(host_name,db_name,user_name,user_password)
    cur = conn.cursor()
    cur.execute('SELECT datname FROM pg_catalog.pg_database')
    table_data = cur.fetchall()
    print("Database: ")
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

