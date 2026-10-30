employees = {
    101: "Rahul Sharma",
    102: "Priya Patel",
    103: "Amit Verma",
    104: "Sneha Mehta"
}

emp_id = int(input("Enter Employee ID to update: "))

if emp_id in employees:
    new_name = input("Enter new Employee Name: ")
    employees[emp_id] = new_name
    print("Employee name updated successfully.")
else:
    print("Employee ID not found.")

print("Updated Dictionary:", employees)
