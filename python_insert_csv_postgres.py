#!/usr/local/bin/python3.7

import subprocess
import os
import csv
import fnmatch
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

#status, result = subprocess.getstatusoutput('ls -l /root/python/all-network-04.csv')


file_name = input("Eneter filename: ")
db_name = input("Enter database name: ")
table_name = input("Enter table name to create: ")

if (os.path.isfile(file_name.strip())):
        if fnmatch.fnmatch(file_name,'*.csv'):
             #df = pd.read_csv('all-network-04.csv')

             conn = pg.connect(host='localhost', dbname=db_name, user='postgres', password='redhat')
             table_data = pd.read_sql('SELECT datname FROM pg_catalog.pg_database',conn)
             cur = conn.cursor()
             cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (table_name,))
             if cur.fetchone()[0] is not "True":
                   df = pd.read_csv(file_name)
                   df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces
                   engine = create_engine('postgresql://postgres:redhat@localhost:5432/testdb')
                   df.to_sql(table_name, engine)
             else:
                   print("The table ", table_name, "already exist")
        else:
             print("The ",file_name," is not is csv format")
else:
    print("The ", file_name," not exist")

