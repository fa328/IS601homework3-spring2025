'''My Calculator Test'''
from calculator.calculation import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''Calculations functions'''

    @staticmethod
    def add(a: float, b: float) -> str:
        '''Test that addition function works '''    
        calculation = Calculations(a, b, add)
        return calculation.get_result()

    @staticmethod
    def subtract(a: float, b: float) -> str:
        '''Test that subtract function works '''    
        calculation = Calculations(a, b, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(a: float, b: float) -> str:
        '''Test that multiply function works '''    
        calculation = Calculations(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a: float, b: float) -> str:
        '''Test that divide function works '''    
        if b == 0:
            return "Error: Division by zero"
        return Calculations(a, b, divide).get_result()

class CalculationsHistory:
    '''To store history'''
    history = []

    @classmethod
    def add_history(cls, calculation):
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
