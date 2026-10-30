# Practical 45: Shopping list menu-driven program

shopping_list = []

while True:
    print("\n--- SHOPPING LIST MENU ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Search Item")
    print("4. Update Item")
    print("5. Sort Items")
    print("6. Display List")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        item = input("Enter item name to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' added to list.")
    elif choice == '2':
        item = input("Enter item name to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed.")
        else:
            print("Item not found!")
    elif choice == '3':
        item = input("Enter item name to search: ").strip()
        if item in shopping_list:
            print(f"'{item}' found at position {shopping_list.index(item) + 1}.")
        else:
            print("Item not found!")
    elif choice == '4':
        old_item = input("Enter item name to update: ").strip()
        if old_item in shopping_list:
            idx = shopping_list.index(old_item)
            new_item = input("Enter new item name: ").strip()
            shopping_list[idx] = new_item
            print("Item updated successfully.")
        else:
            print("Item not found!")
    elif choice == '5':
        shopping_list.sort()
        print("Shopping list sorted alphabetically.")
    elif choice == '6':
        print("Current Shopping List:", shopping_list)
    elif choice == '7':
        print("Exiting Shopping List program. Bye!")
        break
    else:
        print("Invalid choice, please select between 1 and 7.")
