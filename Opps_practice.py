class Calculator:
    def __init__(self, num1, num2):
        # Initialize the attributes num1 and num2
        self.num1 = num1
        self.num2 = num2

    def add(self):
        # Return the sum of num1 and num2
        print("Addition Result :", self.num1 + self.num2 )

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self, factor):
       return self.num1 * factor

    def divide(self, divisor):
       if divisor == 0:
        raise ZeroDivisionError
       else:
        return self.num1 / divisor 

                    

calculator = Calculator(10, 5)
calculator.add()
print("Subtraction Result:", calculator.subtract())
print("Multiplication Result:", calculator.multiply(3))
print("Division Result:", calculator.divide(0))
