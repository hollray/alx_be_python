# This program calculates the age of a person"
# Program written by Joshua Odedeyi
# Date: 2025-May-23
age = int(input("How old are you?"))
current_year = 2023
# This gives the user the option to chose the year they want to check
future_year = int(input("Enter the year you want to know your age in: "))
# This calculates the future age by subtracting the current year from the future year and adding the current age
future_age = future_year - current_year + age
# This prints the future age of the user
# this line converts future age to string
future_year = str(future_year) + str(",")
print("In", future_year, "you will be", future_age, "years old.")
