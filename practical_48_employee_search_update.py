# Practical 48: Employee search and update

employees = ["Rahul", "Priya", "Amit", "Sneha", "Vikas"]
print("Current employees:", employees)

search_name = input("Enter employee name to search: ").strip()

found = False
for i in range(len(employees)):
    if employees[i].lower() == search_name.lower():
        found = True
        new_name = input(f"'{employees[i]}' found. Enter new name to update: ").strip()
        employees[i] = new_name
        print("Employee name updated.")
        break

if not found:
    print(f"'{search_name}' not found. Adding to employee list.")
    employees.append(search_name)

print("Updated employee list:", employees)
