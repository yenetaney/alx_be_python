def safe_divide(numerator, denominator):
    try:
        numerator = int(numerator)
        denominator = int(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter valid numbers."