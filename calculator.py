"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def add(a, b): 
    return a+b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a ==0:
            raise ZeroDivisionError
        return b/a
    except:
        return ZeroDivisionError

def log(a, b):
    try:
        if a <= 0:
            raise ValueError
        elif b <=1:
            raise ValueError
        return math.log(b,a)
    except:
        return ValueError

def exp(a, b):
    return a**b



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