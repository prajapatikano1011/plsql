# Practical 50: Nested list of student details [Roll No, Name, Marks]

students = [
    [101, "Aarav", 85],
    [102, "Bhavna", 92],
    [103, "Chirag", 78],
    [104, "Divya", 95],
    [105, "Eshan", 88]
]

print("Original student records:")
for s in students:
    print(s)

# Sort students according to marks in descending order
students.sort(key=lambda x: x[2], reverse=True)

print("\nStudents sorted by marks (Highest first):")
for s in students:
    print(f"Roll: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

topper = students[0]
print(f"\nTopper Details -> Roll No: {topper[0]}, Name: {topper[1]}, Marks: {topper[2]}")
