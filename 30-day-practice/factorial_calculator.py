#!/bin/python3

"""
Factorial calculator of a non-negative integer using recursion
A factorial of a non-negative number is defined as n! and is the product of all the 
positive integers les than, or equal to n
5! = 5 x 4 x 3 x 2 x 1
Per definition 0! = 1

Recursion is a programming technique where a function calls itself to solve smaller
issue. Its useful for math operations such as factorials. Recursion needs two things:
base case -- stops recursion
recursion case -- calls function with a smaller value

per problem definition:
n has to be integer
n has to be a positive number
n == 0, return 1 ===> Base case
n > 0, return factorial(n-1) ===> recursive case
"""

def calculation():

    try:
        # --- Pre-flight check: int type ---
        n = int(input("\nEnter a non-negative integer to calculate its factorial:\n"))
        
        # --- Pre-flight check: positive number---
        if n < 0:
            print("Please enter a non-negative integer")
        else:

            def factorial(n):
                if n == 0:
                    return 1
                else:
                    return n * factorial(n-1) 
            
            result = factorial(n)
            print(f"\nThe factorial of number {n} is {result}\n")

    except ValueError:
        print("Please enter a valid integer")


if __name__ == '__main__':
    calculation()
