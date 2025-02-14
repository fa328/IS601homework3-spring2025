<<<<<<< HEAD
'''Calculations functions'''
=======
<<<<<<< HEAD
"""My level 3 Calcu"""

def add(a, b):
    """Test that addition function works."""
    return a + b

def subtract(a, b):
    """Test that subtraction function works"""
    return a - b

def multiply(a, b):
    """Test that multiply fuction works"""
    return a * b

def divide(a, b):
    """Test that divide fuction works"""
    return a / b
=======
'''My Calculator Test'''
<<<<<<< HEAD
>>>>>>> Main
=======
import pytest # type: ignore
>>>>>>> part3
from calculator.calculation import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''Calculations functions'''
<<<<<<< HEAD
    @staticmethod
    def add(a,b):
        '''Test that addition function works '''    
        calculation = Calculations(a, b, add) # add function
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        '''Test that subtract function works '''    
        calculation = Calculations(a, b, subtract) # subtract function
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        '''Test that multiply function works '''    
        calculation = Calculations(a, b, multiply) # multiply fuction
        return calculation.get_result()
    @staticmethod
    def divide (a,b):
        '''Test that addition function works '''    
        calculation = Calculations(a, b, divide) # divide fuction
        return calculation.get_result()
=======

    @staticmethod
    def add(a: float, b: float) -> float:
        '''Test that addition function works '''    
        calculation = Calculations(a, b, add)
        return calculation.get_result()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        '''Test that subtract function works '''    
        calculation = Calculations(a, b, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        '''Test that multiply function works '''    
        calculation = Calculations(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a: float, b: float) -> float:
        '''Test that divide function works '''    
        if b == 0:
            return "Error: Division by zero"
        return Calculations(a, b, divide).get_result()

class CalculationsHistory:
    '''To store history'''
    history = []

    @classmethod
    def add_history(cls, calculation: float):
        '''Performs addition, subtraction, multiplication, division'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        '''To get the history of calculations'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Use to clears the history'''
        cls.history = []
<<<<<<< HEAD

calc = Calculator()
result = calc.add(2, 2)
CalculationsHistory.add_history(result)
print(CalculationsHistory.get_history())
=======
>>>>>>> part3
>>>>>>> Main
