# Program to draw patterns by the number of times defined by user

length_of_square = int(input("Enter the size of the pattern:"))
i = 0
while i < length_of_square:
    j = 0
    for j in range(length_of_square):
        print("*", end=" ")
        j += 1
    print()  # Move to the next line after printing one row
    i += 1
# This will print a square pattern of asterisks
# The user can define the size of the square pattern by entering a number
