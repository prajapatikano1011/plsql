# Practical 13: Remove duplicates from a list

numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print("Original list:", numbers)

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)
