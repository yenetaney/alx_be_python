class Calculator:
    calculation_type = "Arithmetic Operations"

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    @staticmethod
    def multiply(a, b):
        return a + b


