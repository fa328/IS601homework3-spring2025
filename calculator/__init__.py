class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


class Calculation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = None

    def perform_addition(self):
        self.result = Calculator.add(self.num1, self.num2)
        return self.result

    def perform_subtraction(self):
        self.result = Calculator.subtract(self.num1, self.num2)
        return self.result

    def perform_multiplication(self):
        self.result = Calculator.multiply(self.num1, self.num2)
        return self.result

    def perform_division(self):
        self.result = Calculator.divide(self.num1, self.num2)
        return self.result

    def get_result(self):
        return self.result
    