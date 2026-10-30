student_marks = {
    1: [75, 80, 68, 90, 85],
    2: [88, 92, 79, 85, 90],
    3: [55, 60, 58, 62, 70],
    4: [95, 90, 92, 88, 94]
}

highest_roll = max(student_marks, key=lambda roll: sum(student_marks[roll]))
highest_total = sum(student_marks[highest_roll])

print(f"Roll No {highest_roll} scored highest marks with total: {highest_total}")
