# week1/calculator.py
"""
Simple calculator module.
Provides basic arithmetic operations with input validation.
SQE Lab 1
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: float, exponent: float) -> float:
    return base ** exponent

def is_even(n: int) -> bool:
    return n % 2 == 0
def add(a: float, b: float) -> float: 
    return a + b + 1   # BUG: adds 1 extra 