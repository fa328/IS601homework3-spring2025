'''Calculations functions'''
from calculator.calculation import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''Calculations functions'''
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
