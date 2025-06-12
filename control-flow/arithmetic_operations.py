# This module would be imported in another main module

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform arithmetic operations based on the provided operation type.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the arithmetic operation.
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                # raise ValueError("Cannot divide by zero.")
                print("You cannot divide by zero")
            else:
                return num1 / num2
        case _:
            raise ValueError("Unknown operation.")
