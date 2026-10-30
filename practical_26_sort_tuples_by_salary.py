employees = [("Rahul", 45000), ("Priya", 75000), ("Amit", 30000), ("Sneha", 62000)]
sorted_employees = sorted(employees, key=lambda emp: emp[1])
print(sorted_employees)
