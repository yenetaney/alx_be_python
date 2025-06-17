shopping_list = []
#Implement functionality to add items to the list, remove items, and display the current list.

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Quit")

def add_item():
    item = input("enter item to add: ")
    shopping_list.append(item)
    print(f"{item} has add to the list")
def remove_item():
    item = input("enter item to remove: ")
    if item in shopping_list:
         shopping_list.remove(item)
         print(f"{item} removed from the list")
    else:
        print(f"{item} not found in the list")
def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is empty.")


while True:
    display_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print(f"Wrong input, please enter a number from 1-4. You entered '{choice}'")

    print(f"You entered: '{choice}'")  # Debug info