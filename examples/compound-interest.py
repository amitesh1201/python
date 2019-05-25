#!/usr/bin/python3.6


principle_amount = input("Enter the amount: ")
rate = 3.875
time = input("Enter the number of years for entered amount: ")


CI = float(principle_amount) * (pow((1 + rate / 100), int(time)))
print("The compound interest is: ", CI)