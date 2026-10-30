student_data = {}

for i in range(5):
    roll = int(input(f"Enter roll no for student {i+1}: "))
    raw_marks = input("Enter 6 marks out of 50 (comma separated): ")
    marks = [float(m.strip()) for m in raw_marks.split(",")]
    student_data[roll] = marks

subject_stats = {}

for sub_idx in range(6):
    sub_marks = [student_data[r][sub_idx] for r in student_data]
    subject_stats[f"Subject_{sub_idx + 1}"] = {
        "min": min(sub_marks),
        "max": max(sub_marks)
    }

print("
Subject-wise Min and Max Marks:")
for sub, stats in subject_stats.items():
    print(f"{sub}: Min = {stats['min']}, Max = {stats['max']}")
