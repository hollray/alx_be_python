# This modle uses datetime library to explore datetime objects and their properties.
import datetime


def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()

    # Display the current date and time
    # print("Current date and time:", current_date)
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


# Calling the Function that displays the current date and time
display_current_datetime()

number_of_days = int(
    input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))


# Calling the Function that calculates the future date
calculate_future_date()
