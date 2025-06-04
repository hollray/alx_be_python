# This calculator Program will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division)
# Then then perform the selected operation using a Match Case statement and display the result.
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    case _:  # Default case for invalid operation:
        result = "Invalid operation selected"
        exit()
print(f"The result is {result}.")
