"""
Recursion - When a function calls itself to solve a problem by breaking it 
    into smaller, similar sub-problems.

## Basic idea
Every recursive function must have two parts:
Base case -> stops the recursion
Recursive case -> the function calls itself
Without a base case, recursion will run forever and cause a RecursionError.


## Example: Factorial Calculation
### Factorial of n (written n!) is:
    n! = n * (n-1) * (n-2) * ... * 1
### Base case: 0! = 1 and 1! = 1
### Recursive case: n! = n * (n-1)!
"""

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


## Example: Fibonacci Sequence
### Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
### Base case: fib(0) = 0, fib(1) = 1     
### Recursive case: fib(n) = fib(n-1) + fib(n-2)
def fib(n):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(6))  # Output: 8
print(fib(7))  # Output: 13