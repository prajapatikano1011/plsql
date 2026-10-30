# Practical 51: Menu-driven program for all list operations

my_list = [10, 20, 30, 40]

while True:
    print("\n=== LIST OPERATIONS MENU ===")
    print("1. Append      2. Insert      3. Extend      4. Remove")
    print("5. Pop         6. Sort        7. Reverse     8. Count")
    print("9. Index       10. Copy       11. Clear      12. Display")
    print("13. Exit")

    ch = input("Enter choice (1-13): ").strip()

    if ch == '1':
        val = int(input("Enter value to append: "))
        my_list.append(val)
    elif ch == '2':
        idx = int(input("Enter index: "))
        val = int(input("Enter value: "))
        my_list.insert(idx, val)
    elif ch == '3':
        items = list(map(int, input("Enter space-separated elements to extend: ").split()))
        my_list.extend(items)
    elif ch == '4':
        val = int(input("Enter value to remove: "))
        if val in my_list:
            my_list.remove(val)
        else:
            print("Value not found.")
    elif ch == '5':
        if my_list:
            removed = my_list.pop()
            print("Popped item:", removed)
        else:
            print("List is empty.")
    elif ch == '6':
        my_list.sort()
        print("List sorted.")
    elif ch == '7':
        my_list.reverse()
        print("List reversed.")
    elif ch == '8':
        val = int(input("Enter value to count: "))
        print("Count:", my_list.count(val))
    elif ch == '9':
        val = int(input("Enter value to get index: "))
        if val in my_list:
            print("Index:", my_list.index(val))
        else:
            print("Value not in list.")
    elif ch == '10':
        copied = my_list.copy()
        print("Copied list:", copied)
    elif ch == '11':
        my_list.clear()
        print("List cleared.")
    elif ch == '12':
        print("Current list:", my_list)
    elif ch == '13':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
