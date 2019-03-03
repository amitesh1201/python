#!/usr/local/bin/python3.7

import subprocess
import os
import psycopg2
import pandas as pd

#conn = psycopg2.connect(database = "all_network", user = "postgres", password = "redhat", host = "127.0.0.1", port = "5432")
#status, conn = subprocess.getstatusoutput('psycopg2.connect(user = "'"postgres"'", password = "'"redhat"'", host = "'"127.0.0.1"'", port = "'"5432"'", database = "'"testdb"'")')
#status, result = subprocess.getstatusoutput('ls -l /root/python/all-network-04.csv')

#print (status)
#print("connected")

file_name = input("Eneter filename: ")
table_name = input("Enter table name to create: ")

#df = pd.read_csv('all-network-04.csv')
df = pd.read_csv(file_name)
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:redhat@localhost:5432/testdb')

df.to_sql(table_name, engine)
