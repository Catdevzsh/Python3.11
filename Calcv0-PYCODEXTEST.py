from typing import Tuple

def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

def divide(x: float, y: float) -> float:
    """Divide two numbers."""
    return x / y

def get_user_input() -> Tuple[float, float, str]:
    """Get user input for two numbers and choice of operation."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose your operation (1/2/3/4): ")
    return num1, num2, operation

def perform_operation(num1: float, num2: float, operation: str) -> float:
    """Perform the selected operation on the two numbers."""
    if operation == '1':
        return add(num1, num2)
    elif operation == '2':
        return subtract(num1, num2)
    elif operation == '3':
        return multiply(num1, num2)
    elif operation == '4':
        return divide(num1, num2)
    else:
        raise ValueError("Invalid operation choice.")

def print_result(result: float, num1: float, num2: float, operation: str) -> None:
    """Print the result of the operation."""
    op_dict = {'1': '+', '2': '-', '3': '*', '4': '/'}
    op_symbol = op_dict[operation]
    print(f"{num1} {op_symbol} {num2} = {result}")

try:
    num1, num2, operation = get_user_input()
    result = perform_operation(num1, num2, operation)
    print_result(result, num1, num2, operation)
except ValueError as e:
    print(str(e))
except KeyboardInterrupt:
    print("Program interrupted by user.")
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("Program completed successfully.")
finally:
    print("404: Program execution terminated.")
