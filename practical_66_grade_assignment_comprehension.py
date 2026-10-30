# Practical 66: Assign grades using list comprehension

marks_list = [95, 82, 67, 45, 33, 76, 89, 58]

def get_grade(m):
    if m >= 90:
        return 'A'
    elif m >= 75:
        return 'B'
    elif m >= 60:
        return 'C'
    elif m >= 40:
        return 'D'
    else:
        return 'F'

grades = [(m, get_grade(m)) for m in marks_list]

print("Marks and Grades:")
for m, g in grades:
    print(f"Marks: {m} -> Grade: {g}")
