from calculator.calculation import Calculation
from calculator.operation import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add) # add function
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        Calculation = Calculation(a, b, subtract) # subtract function
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        Calculation = Calculation(a, b, multiply) # multiply fuction
        return calculation.get_result()
    @staticmethod
    def divide (a,b):
        Calculation = Calculation(a, b, divide) # divide fuction
        return calculation.get_result()

