# This program is a simple daily reminder to users to take a break and stretch.
# It uses conditional statements,

task = input("Enter your task:\n")
priority = input("Priority (high/medium/low):\n")
time_bound = input("Is it time-bound? (yes/no):\n")
message = " "

match priority:
    case "high":
        # print("This is a high-priority task.")
        message = "high"
    case "medium":
        message = "medium"
    case "low":
        message = "low"
    case _:
        print("Unknown priority.")
# and a match-case structure to categorize tasks.
if time_bound.lower() == "yes":
    print(
        f"Reminder: {task} is a {message} priority task that requires immediate attention today!")
elif time_bound.lower() == "no":
    print(
        f"Note: {task} is a {message} priority task. Consider completing it when you have free time.")
else:
    print("Invalid input for time-bound status. Please enter 'yes' or 'no'.")
