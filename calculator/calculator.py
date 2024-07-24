class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0 or a == 0:
            raise ZeroDivisionError("Divsion by zero error")
        else:
            return a / b


