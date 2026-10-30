# Practical 15: Find the average of numbers in a list

marks = [78, 85, 92, 65, 88]
print("Marks:", marks)

total = 0
for m in marks:
    total += m

avg = total / len(marks)
print("Average mark is:", avg)
