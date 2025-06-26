class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        result = a + b
        print(f"The sum is: {result}")
        return result
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        result = a * b
        print(f"The product is: {result}")
        return result


