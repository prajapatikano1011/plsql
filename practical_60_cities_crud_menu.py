# Practical 60: CRUD operations on list of cities

cities = ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]

while True:
    print("\n--- CITIES CRUD MENU ---")
    print("1. Create (Add City)")
    print("2. Read (View All Cities)")
    print("3. Update City Name")
    print("4. Delete City")
    print("5. Exit")

    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        city = input("Enter city name: ").strip()
        cities.append(city)
        print(f"'{city}' added successfully.")
    elif choice == '2':
        print("List of Cities:")
        for idx, c in enumerate(cities, 1):
            print(f"{idx}. {c}")
    elif choice == '3':
        old_name = input("Enter city to update: ").strip()
        if old_name in cities:
            pos = cities.index(old_name)
            new_name = input("Enter new name: ").strip()
            cities[pos] = new_name
            print("City updated successfully.")
        else:
            print("City not found!")
    elif choice == '4':
        city = input("Enter city to delete: ").strip()
        if city in cities:
            cities.remove(city)
            print("City deleted successfully.")
        else:
            print("City not found!")
    elif choice == '5':
        print("Exiting CRUD program.")
        break
    else:
        print("Invalid choice, try again.")
