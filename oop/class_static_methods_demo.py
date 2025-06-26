class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        result = a + b
        print(f"The sum is: {result}")
        return result
    
    @staticmethod
    def multiply(a, b):
        return a * b


