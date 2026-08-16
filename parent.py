# """
# MINIMAL OOPS PROGRAM FOR ADDITION USING LAMBDA
# """

# class Addition:
#     def __init__(self):
#         # Lambda for addition
#         self.add = lambda x, y: x + y
    
#     def calculate(self, a, b):
        # result = self.add(a, b)
        # print(f"{a} + {b} = {result}")
        # return result

# Test the program
# if __name__ == "__main__":
#     print("=== SIMPLE ADDITION ===")
    
#     # Create object
#     calc = Addition()
    
#     # Perform additions
#     calc.calculate(5, 3)      # Output: 5 + 3 = 8
#     calc.calculate(10, 20)    # Output: 10 + 20 = 30
#     calc.calculate(100, 50)   # Output: 100 + 50 = 150
#     calc.calculate(7.5, 2.5)  # Output: 7.5 + 2.5 = 10.0

#------------------------------------>
class DataCalculator:
    """Parent class for processing two numerical data values."""

    def __init__(self, data1: float, data2: float):
        self.data1 = float(data1)
        self.data2 = float(data2)

    def add(self) -> float:
        """Returns the sum of the two numbers."""
        return self.data1 + self.data2

    def subtract(self) -> float:
        """Returns data1 minus data2."""
        return self.data1 - self.data2

    def multiply(self) -> float:
        """Returns the product of the two numbers."""
        return self.data1 * self.data2

    def divide(self) -> float:
        """Returns data1 divided by data2, handling zero division."""
        if self.data2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return self.data1 / self.data2
