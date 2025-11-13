"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    pass

import math

# 1. Addition
def add(a, b):
    return a + b

# 2. Subtraction
def subtract(a, b):
    return a - b

# 3. Multiplication
def multiply(a, b):
    return a * b

# 4. Division
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# 5. Logarithm
def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)

# 6. Exponent
def exponent(a, b):
    return a ** b