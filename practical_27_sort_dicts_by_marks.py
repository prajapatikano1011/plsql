students = [
    {"name": "Aarav", "marks": 85},
    {"name": "Bhavna", "marks": 92},
    {"name": "Chirag", "marks": 78},
    {"name": "Divya", "marks": 95}
]
sorted_students = sorted(students, key=lambda s: s["marks"])
print(sorted_students)
