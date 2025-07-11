# Python script to calculate temperature conversions between Celsius and Fahrenheit using global variables.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


temperature_value = float(input("Enter the temperature to convert: "))
conversion_type = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

# User Interaction and Input Validation
try:
    # Prompt the user for temperature (matching the required prompt exactly)
    temperature_value_str = input("Enter the temperature to convert: ")

    # Convert input to float. This might raise a ValueError if the input is not numeric.
    temperature_value = float(temperature_value_str)

    # Prompt for conversion type (matching the required prompt exactly)
    conversion_type = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform conversion based on input
    if conversion_type == "C":
        converted_value = convert_to_fahrenheit(temperature_value)
        print(f"{temperature_value}°C is {converted_value}°F")
    elif conversion_type == "F":
        converted_value = convert_to_celsius(temperature_value)
        print(f"{temperature_value}°F is {converted_value}°C")
    else:
        # Handle invalid conversion type input
        print("Invalid conversion type. Please enter 'C' or 'F'.")

# Catch ValueError if the user input for temperature is not numeric
except ValueError:
    # Output the exact error message required by the checker
    print("Invalid temperature. Please enter a numeric value.")
