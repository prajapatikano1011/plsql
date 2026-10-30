text = input("Enter a string: ")

while True:
    print("\n--- STRING MANIPULATION MENU ---")
    print("a. Find length")
    print("b. Convert to uppercase")
    print("c. Convert to lowercase")
    print("d. Initial capital (title)")
    print("e. Split the string")
    print("f. Exit")

    choice = input("Enter choice (a-f): ").strip().lower()

    if choice == 'a':
        print("Length:", len(text))
    elif choice == 'b':
        print("Uppercase:", text.upper())
    elif choice == 'c':
        print("Lowercase:", text.lower())
    elif choice == 'd':
        print("Title case:", text.title())
    elif choice == 'e':
        print("Split:", text.split())
    elif choice == 'f':
        print("Exiting.")
        break
    else:
        print("Invalid choice, please try again.")
