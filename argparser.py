#!/usr/bin/python3.6

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--ipaddr', type=str, help='Ipaddress')
parser.add_argument('--api-port', type=int, help='API port')
parser.add_argument('--tcp-port', type=int, help='TCP port')
parser.add_argument('--user',type=str, help='Rabbitmq user')
parser.add_argument('--password',type=str, help='Rabbitmq user password')
#parser.add_argument('positionals', nargs='*')
args = parser.parse_args()
#print(args.positionals, args.empid)
try:

  print(args.ipaddr)
  print(args.api-port)
  print(args.tcp-port)
  print(args.user)
  print(args.password)
except:
   parser.print_help()
   print("Error")
