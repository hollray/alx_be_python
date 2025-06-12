# This module manages shopping lists by allowing users to add, remove, and view items.
shopping_list = []
shopping = (input("What do you want to do? pick th following options (1 to Add Item, 2 to Remove Item, 3 to View the list and 4 to Exit)"))

while shopping != 4:
    match shopping:
        case "1":
            item = (input("What Item do you want to add to the list? "))
            shopping_list.append(item)
        case "2":
            item = (input("What Item do you want to remove from the list? "))
            shopping_list.remove(item)
        case "3":
            print("Shopping List: ")
            for item in shopping_list:
                print(f"- {item}")
        case "4":
            print("You have chossen to exit the program")
            shopping = int(4)
            break
            # exit

        case _:
            print("Invalid option. Please try again.")

    shopping = (input(
        "What do you want to do? pick th following options (1 to Add Item, 2 to Remove Item, 3 to View the list and 4 to Exit)"))
