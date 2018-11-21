#!/usr/bin/python3.6

# This script perform the maths operations.

import os
from sys import exit

global menu_condition

def addition(num1,num2):
    result = num1 + num2
    return result

def substration(num1,num2):
    result = num1 - num2
    return result

def multiplication(num1,num2):
    result = num1 * num2
    return result

def devision(num1,num2):
    if num2 == 0:
       print ("Denominator should not be zero")
       exit()

    result = num1 / num2
    return result

def menu():
    menu_condition = 0
    while menu_condition == 0:
        print("Select the choice for operations")
        print("Select 1 for addition")
        print("select 2 for substration")
        print("select 3 for multiplication")
        print("select 4 for devision")
        print("select 5 for exit")


        menu_condition = input("Select the choice: ")

        if menu_condition == 5:
            exit()

        num1 = input("Enter num1: ")
        num2 = input("Enter num2: ")
        if menu_condition == 1:
            result = addition(num1,num2)
            print ("The addition of ", num1 ,"+",num2,"is",result)
        elif menu_condition == 2:
            substration(num1,num2)
            print ("The substration of ", num1, "-", num2, "is", result)
        elif menu_condition == 3:
            multiplication(num1,num2)
            print ("The multiplication of ", num1, "*", num2, "is", result)
        elif menu_condition == 4:
            devision(num1,num2)
            print ("The devision of ", num1, "/", num2, "is", result)
        else:
            print("Select choice from the menu")


### Main ###

menu()
