"""
Factorial of a positive integer N using:
1. Recursion
2. Iteration
"""

def recursive_factorial(n):
    """
    Return the factorial of integer n
    >>> recursive_factorial(-21)
    "Invalid. Factorial doesn't exist for negative numbers."
    >>> recursive_factorial(10)
    3628800
    >>> recursive_factorial(5)
    120
    """
    if n<0:
        return f"Invalid. Factorial doesn't exist for negative numbers."
    if n==0:
        return 1
    return n*recursive_factorial(n-1)

def iterative_factorial(n):
    """
    Return the factorial of integer n
    >>> iterative_factorial(-2)
    "Invalid. Factorial doesn't exist for negative numbers."
    >>> iterative_factorial(9)
    362880
    >>> iterative_factorial(8)
    40320
    """
    if n<0:
        return f"Invalid. Factorial doesn't exist for negative numbers."
    factorial = 1
    for i in range(1,n+1):      #integers from [1,n+1) or [1,n]
        factorial *= i
    return factorial
    
