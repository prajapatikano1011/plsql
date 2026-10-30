employees = {
    101: "Rahul Sharma",
    102: "Priya Patel",
    103: "Amit Verma",
    104: "Sneha Mehta"
}

emp_id = int(input("Enter Employee ID: "))

if emp_id in employees:
    print("Employee Name:", employees[emp_id])
else:
    new_name = input("Employee ID not found. Enter Employee Name to add: ")
    employees[emp_id] = new_name
    print("Employee added successfully.")

print("Updated Dictionary:", employees)
