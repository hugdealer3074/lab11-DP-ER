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

print(add(2,2))
print(sub(2,2))
print(mul(2,2))
print(div(0,4))
print(log(2,2))
print(exp(2,2))




