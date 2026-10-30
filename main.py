import module as m1

while True:
    print("\n*** PRODUCT MANAGEMENT SYSTEM ***")
    print("1. Add Product")
    print("2. Dispaly")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. sort")
    print("7. Exit")

    choice = input("enter your choice(1-6):")
    print("------------------------------------")

    if choice == "1":
            m1.add()
    elif choice == "2":
            m1.display()
    elif choice == "3":
            m1.updateName()
    elif choice == "4":
            m1.deletebyPId()
    elif choice == "5":
            m1.search()
    elif choice == "6":
            m1.sortbyprice()
    elif choice == "7":
            print("exiting application. Goodbye!")
            break
    else:
           print("invalid option selected. please choose between 1 and 6")