from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """Encapsulates a single calculation."""
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        # call
        return self.operation(self.a, self.b)

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

