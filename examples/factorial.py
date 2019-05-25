#!/usr/bin/python3.6

#    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

def factorial(n):
     if (n == 1 or n == 0):
         return 1
     else:
         fact = n * factorial(n - 1)
         return fact


num = input("Enter number to find factorial: ");

print("Factorial of",num,"is",factorial(int(num)))



