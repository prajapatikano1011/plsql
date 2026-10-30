employees = {
    101: "Rahul Sharma",
    102: "Priya Patel",
    103: "Amit Verma",
    104: "Sneha Mehta"
}

emp_id = int(input("Enter Employee ID to remove: "))

if emp_id in employees:
    removed_name = employees.pop(emp_id)
    print(f"Employee {removed_name} (ID: {emp_id}) removed successfully.")
else:
    print("Employee ID not found.")

print("Updated Dictionary:", employees)
