student_marks = {
    1: [75, 80, 68, 90, 85],
    2: [88, 92, 79, 85, 90],
    3: [55, 60, 58, 62, 70],
    4: [95, 90, 92, 88, 94]
}

results = {}

for roll, marks in student_marks.items():
    total = sum(marks)
    percentage = total / len(marks)
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 75:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'
        
    results[roll] = (total, percentage, grade)

print("Results dictionary (Total, Percentage, Grade):")
for roll, res in results.items():
    print(f"Roll No {roll}: Total={res[0]}, Percentage={res[1]:.2f}%, Grade={res[2]}")
