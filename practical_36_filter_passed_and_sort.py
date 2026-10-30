students = [("Aarav", 85), ("Ravi", 32), ("Bhavna", 92), ("Mohit", 38), ("Divya", 74)]
passed_students = sorted(filter(lambda s: s[1] >= 40, students), key=lambda s: s[1])
print(passed_students)
