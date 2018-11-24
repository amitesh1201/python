#!/usr/bin/python3.6

import os
from sys import exit

class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee", Employee.empCount)


    def displayEmployee(self):
        print("Name: ", self.name)
        print("Salary", self.salary)

global flag

name = input("Enter name: ")
salary = input("Enter salary: ")
flag = 'y'
while flag == 'y':
   emp1 = Employee(name,salary)
   emp1.displayEmployee()
   flag = input("Do you wish to continue (y/n): ")
   if flag != 'y':
       break
   name = input("Enter name: ")
   salary = input("Enter salary: ")
#emp2 = Employee("Swapnilz",150000)
#emp2.displayEmployee()

print(Employee.empCount)