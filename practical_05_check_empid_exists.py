employees = {
    101: "Rahul Sharma",
    102: "Priya Patel",
    103: "Amit Verma",
    104: "Sneha Mehta"
}
emp_id = int(input("Enter Employee ID: "))

if emp_id in employees:
    print(f"Employee ID {emp_id} exists in the dictionary.")
else:
    print(f"Employee ID {emp_id} does not exist in the dictionary.")
