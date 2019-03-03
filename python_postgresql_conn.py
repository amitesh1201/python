#!/usr/local/bin/python3.7

import psycopg2

conn = psycopg2.connect(database = "all_network", user = "postgres", password = "redhat", host = "127.0.0.1", port = "5432")
print("connected")
