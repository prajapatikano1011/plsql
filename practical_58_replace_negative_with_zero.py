# Practical 58: Replace every negative number with zero

numbers = [12, -7, 45, -3, 0, -18, 29]
print("Original list:", numbers)

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print("List after replacing negative numbers:", numbers)
