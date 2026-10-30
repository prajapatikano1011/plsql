# Practical 43: Operations on 10 student marks

marks = [65, 82, 45, 90, 74, 58, 88, 71, 93, 60]
print("Initial marks:", marks)

# Insertion
marks.append(79)
print("After insertion (append 79):", marks)

# Deletion
marks.remove(45)
print("After deleting mark 45:", marks)

# Updating
marks[0] = 70
print("After updating first mark to 70:", marks)

# Sorting
marks.sort()
print("Sorted marks:", marks)

# Reversing
marks.reverse()
print("Reversed marks:", marks)

# Calculations
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.2f}")
