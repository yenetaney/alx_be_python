# math_operations.py
def perform_operation(num1, num2, operation):
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"  # Returning a recognizable message
        return num1 / num2
 
    else:
        raise ValueError("Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'.")