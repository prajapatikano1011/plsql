# Practical 16: Find second largest and second smallest number

numbers = [45, 12, 89, 34, 78, 23]
print("List:", numbers)

# Remove duplicates if any
unique_nums = list(set(numbers))
unique_nums.sort()

if len(unique_nums) >= 2:
    second_smallest = unique_nums[1]
    second_largest = unique_nums[-2]
    print("Second smallest:", second_smallest)
    print("Second largest:", second_largest)
else:
    print("List must have at least 2 distinct numbers.")
