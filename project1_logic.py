from typing import List
import random
import sys

class Calculator:
    @staticmethod
    def add(values: List[float]) -> float:
        if not values:
            raise ValueError("No values provided")
        return sum(values)

    @staticmethod
    def subtract(values: List[float]) -> float:
        if not values:
            raise ValueError("No values provided")
        return values[0] - sum(values[1:])

    @staticmethod
    def multiply(values: List[float]) -> float:
        result = 1
        if not values:
            raise ValueError("No values provided")
        for num in values:
            result *= num
        return result

    @staticmethod
    def divide(values: List[float]) -> float:
        if not values:
            raise ValueError("No values provided")
        if 0 in values[1:]:
            raise ValueError("Cannot divide by 0")
        return values[0] / values[1]

    @staticmethod
    def choose(values: List[float]) -> float:
        if not values:
            raise ValueError("No values provided")
        return random.choice(values)


class CalculatorApp:
    def __init__(self, operator, values):
        self.operator = operator
        self.values = values

    def calculate(self):
        calculator = Calculator()

        if self.operator == 'add':
            return calculator.add(self.values)
        elif self.operator == 'subtract':
            return calculator.subtract(self.values)
        elif self.operator == 'multiply':
            return calculator.multiply(self.values)
        elif self.operator == 'divide':
            return calculator.divide(self.values)
        elif self.operator == 'choose':
            return calculator.choose(self.values)
        else:
            raise ValueError("The operator is missing. Click one of the radio buttons: add, subtract, multiply, divide, choose")