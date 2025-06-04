# This script will ask the user to enter a number,
# It then use a for loop to print the multiplication table for that number from 1 to 10.

number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 11):
    x = number
    z = x * y
    print(f"{x} * {y} = {z}")
