# This program calculates the Financial Expenses of a person in a month
# Program written by Joshua Odedeyi
# Date: 2025-May-24
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_interest_rate = 0.05  # Assuming a 5% annual interest rate
projected_months = int(
    input("Enter the number of months you want to project your savings for: "))
projected_savings = monthly_savings * projected_months + \
    (monthly_savings * projected_months * annual_interest_rate)
print("Your monthly savings are: $", monthly_savings, ".")
print("Projected Savings after", projected_months,
      "months is: $", projected_savings, ".")
