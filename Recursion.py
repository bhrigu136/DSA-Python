"""
Recursion - When a function calls itself to solve a problem by breaking it 
    into smaller, similar sub-problems.

## Basic idea
Every recursive function must have two parts:
Base case -> stops the recursion
Recursive case -> the function calls itself
Without a base case, recursion will run forever and cause a RecursionError.


## Example: Factorial Calculation
# Factorial of n (written n!) is:
n! = n * (n-1) * (n-2) * ... * 1
# Base case: 0! = 1 and 1! = 1
# Recursive case: n! = n * (n-1)!
"""

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120