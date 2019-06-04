#!/usr/bin/python3.6


principle_amount = input("Enter the amount: ")
rate = 3.875
time = input("Enter the number of years for entered amount: ")

SI = (float(principle_amount) * rate * int(time))/100

print("The rate of simple interst is: ", SI)