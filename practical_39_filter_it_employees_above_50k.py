employees = [
    ("Rahul", "IT", 55000),
    ("Priya", "HR", 60000),
    ("Amit", "IT", 45000),
    ("Sneha", "IT", 72000),
    ("Vikas", "Finance", 52000)
]
it_high_salary = list(filter(lambda emp: emp[1] == "IT" and emp[2] > 50000, employees))
print(it_high_salary)
