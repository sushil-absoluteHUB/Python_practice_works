from myproject.parent import DataCalculator


class StatisticalCalculator(DataCalculator):
    """Child class for comparative metrics."""

    def mean(self) -> float:
        return self.add() / 2

    def absolute_difference(self) -> float:
        return abs(self.subtract())

    def ratio(self) -> str:
        return f"{self.data1}:{self.data2}"


# --- Usage Examples ---

# Using ScientificCalculator
sci = StatisticalCalculator(5, 3)
print("Power:", sci.power())  # 5^3 = 125
print("Modulus:", sci.modulus())  # 5 % 3 = 2