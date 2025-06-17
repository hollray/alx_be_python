# Python script to calculate temperature conversions between Celsius and Fahrenheit using global variables.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


temperature_value = float(input("Enter the temperature value: "))
conversion_type = input(
    "The entered Value is it in Celsius or Fahrenheit? (C/F): ").strip().upper()

if conversion_type == "C":
    converted_value = convert_to_fahrenheit(temperature_value)
    print(f"{temperature_value}°C is equal to {converted_value}°F")
elif conversion_type == "F":
    converted_value = convert_to_celsius(temperature_value)
    print(f"{temperature_value}°F is equal to {converted_value}°C")
else:
    print("Invalid conversion type. Please enter 'C' or 'F'.")
