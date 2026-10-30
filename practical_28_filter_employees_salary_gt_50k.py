employees = [
    {"name": "Rahul", "salary": 45000},
    {"name": "Priya", "salary": 75000},
    {"name": "Amit", "salary": 30000},
    {"name": "Sneha", "salary": 62000}
]
high_earners = list(filter(lambda emp: emp["salary"] > 50000, employees))
print(high_earners)
