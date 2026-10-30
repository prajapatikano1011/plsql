# Practical 57: Second largest and second smallest without built-in sort

arr = [45, 12, 89, 23, 77, 10, 95]
print("List:", arr)

# Find first largest and smallest
largest = float('-inf')
second_largest = float('-inf')

smallest = float('inf')
second_smallest = float('inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Smallest:", smallest, "| Second Smallest:", second_smallest)
print("Largest:", largest, "| Second Largest:", second_largest)
