# robust_division_calculator.py
def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors for division by zero and non-numeric inputs.

    Args:
        numerator: String representation of the numerator.
        denominator: String representation of the denominator.

    Returns:
        A string message indicating the result of the division or an error message.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."


if __name__ == "__main__":
    # This block is for testing the function directly (optional)
    num = input("Enter numerator: ")
    den = input("Enter denominator: ")
    print(safe_divide(num, den))
